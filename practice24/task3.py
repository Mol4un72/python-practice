from pathlib import Path
from datetime import datetime
import math
import sys


BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
FILE = DATA / "expenses.csv"
REPORTS = BASE / "reports"
REPORT = REPORTS / "expenses_report.txt"

NAME = "Твоє ім'я та прізвище"
GROUP = "Твоя група"


def usage():
    print("usage: python3 task3.py add <date> <category> <amount> <note>")
    print("       python3 task3.py list")
    print("       python3 task3.py report")


def read_file_lines():
    """Читає файл і в одному місці обробляє помилки самого файлу."""
    try:
        if not FILE.exists():
            raise FileNotFoundError

        if FILE.is_dir():
            raise IsADirectoryError

        with FILE.open("r", encoding="utf-8") as file:
            return file.readlines()

    except FileNotFoundError:
        print(f"error: {FILE} not found", file=sys.stderr)

    except IsADirectoryError:
        print(f"error: {FILE} is a directory, not a file", file=sys.stderr)

    except UnicodeDecodeError:
        print(f"error: {FILE} is not a UTF-8 text file", file=sys.stderr)

    except OSError as error:
        print(f"error: cannot read {FILE}: {error}", file=sys.stderr)

    return None


def validate_record(line):
    """Перевіряє запис і повертає дані або причину помилки."""
    fields = line.split(";")

    if len(fields) != 4:
        return None, f"expected 4 fields, got {len(fields)}"

    date, category, amount_text, note = fields

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None, f"bad date '{date}'"

    try:
        amount = float(amount_text)
    except ValueError:
        return None, f"bad amount '{amount_text}'"

    if not math.isfinite(amount):
        return None, f"bad amount '{amount_text}'"

    if amount <= 0:
        return None, f"amount must be positive, got {amount:.2f}"

    if not category.strip():
        return None, "category is empty"

    return {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }, None


def read_expenses(lines):
    """Повертає коректні витрати й повідомляє про пропущені рядки."""
    expenses = []
    skipped = []

    for number, line in enumerate(lines, start=1):
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        expense, error = validate_record(line)

        if error:
            skipped.append((number, error))
        else:
            expenses.append(expense)

    if skipped:
        print(
            f"skipped {len(skipped)} bad line(s):",
            file=sys.stderr
        )

        for number, reason in skipped:
            print(f"  line {number}: {reason}", file=sys.stderr)

    return expenses


def add_expense(args):
    if len(args) < 5:
        print("error: add needs date, category, amount and note")
        usage()
        return 2

    lines = read_file_lines()

    if lines is None:
        return 1

    date = args[1]
    category = args[2]
    amount_text = args[3]
    note = " ".join(args[4:])

    if ";" in note:
        print("error: note must not contain ';'")
        print("nothing was added")
        return 1

    record, error = validate_record(
        f"{date};{category};{amount_text};{note}"
    )

    if error:
        print(f"error: {error}")
        print("nothing was added")
        return 1

    try:
        with FILE.open("a", encoding="utf-8") as file:
            file.write(
                f"{record['date']};{record['category']};"
                f"{record['amount']:.2f};{record['note']}\n"
            )

    except OSError as error:
        print(f"error: cannot write to {FILE}: {error}", file=sys.stderr)
        return 1

    print(
        f"added: {record['date']} {record['category']} "
        f"{record['amount']:.2f} ({record['note']})"
    )
    return 0


def show_list(expenses):
    print(f"{'date':<12} {'category':<12} {'amount':>8}  note")

    total = 0

    for expense in expenses:
        print(
            f"{expense['date']:<12} "
            f"{expense['category']:<12} "
            f"{expense['amount']:>8.2f}  "
            f"{expense['note']}"
        )
        total += expense["amount"]

    print()
    print(f"{len(expenses)} records, total {total:.2f}")


def make_report(expenses):
    if not expenses:
        print("error: nothing to report, no valid records", file=sys.stderr)
        return 1

    total = sum(expense["amount"] for expense in expenses)

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category] = {"count": 0, "total": 0}

        categories[category]["count"] += 1
        categories[category]["total"] += expense["amount"]

    categories = sorted(
        categories.items(),
        key=lambda item: item[1]["total"],
        reverse=True
    )

    days = {}

    for expense in expenses:
        date = expense["date"]
        days[date] = days.get(date, 0) + expense["amount"]

    top_day = max(days, key=days.get)
    most_expensive = max(expenses, key=lambda item: item["amount"])
    average = total / len(days)

    lines = [
        f"Expenses report for {NAME} ({GROUP})",
        f"Period: {expenses[0]['date']} .. {expenses[-1]['date']}",
        f"Records: {len(expenses)}",
        "",
        f"{'category':<12}{'count':>7}{'total':>12}{'share':>9}  chart",
        "-" * 55
    ]

    for category, data in categories:
        share = data["total"] / total * 100
        chart = "#" * round(share / 5)

        lines.append(
            f"{category:<12}{data['count']:>7}"
            f"{data['total']:>12.2f}{share:>8.1f}%  {chart}"
        )

    lines.extend([
        "-" * 55,
        f"{'total':<12}{len(expenses):>7}{total:>12.2f}{100:>8.1f}%",
        "",
        f"Top day: {top_day} ({days[top_day]:.2f})",
        f"Most expensive: {most_expensive['category']} "
        f"{most_expensive['amount']:.2f} ({most_expensive['note']})",
        f"Average per day: {average:.2f}"
    ])

    result = "\n".join(lines)

    try:
        REPORTS.mkdir(exist_ok=True)
        REPORT.write_text(result, encoding="utf-8")
    except OSError as error:
        print(f"error: cannot save report: {error}", file=sys.stderr)
        return 1

    print(result)
    print()
    print(f"report saved to: {REPORT}")
    return 0


def main():
    args = sys.argv[1:]

    if not args:
        usage()
        return 2

    if args[0] not in ("add", "list", "report"):
        print(f"error: unknown command {args[0]}")
        usage()
        return 2

    if args[0] == "add":
        return add_expense(args)

    if len(args) != 1:
        usage()
        return 2

    lines = read_file_lines()

    if lines is None:
        return 1

    expenses = read_expenses(lines)

    if args[0] == "list":
        show_list(expenses)
        return 0

    return make_report(expenses)


if __name__ == "__main__":
    sys.exit(main())