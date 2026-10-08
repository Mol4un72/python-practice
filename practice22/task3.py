from pathlib import Path
import sys


BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
FILE = DATA / "expenses.csv"
REPORTS = BASE / "reports"
REPORT = REPORTS / "expenses_report.txt"

NAME = "YourName YourSurname"
GROUP = "YourGroup"


def usage():
    print("usage: python3 task3.py add <date> <category> <amount> <note>")
    print("       python3 task3.py list")
    print("       python3 task3.py report")


def add_expense(args):
    if len(args) < 5:
        print("error: add needs date, category, amount and note")
        usage()
        return

    DATA.mkdir(exist_ok=True)

    if not FILE.exists():
        FILE.write_text(
            "# date;category;amount;note\n",
            encoding="utf-8"
        )

    date = args[1]
    category = args[2]

    try:
        amount = float(args[3])
    except ValueError:
        print("error: amount must be a number")
        usage()
        return

    note = " ".join(args[4:])

    with FILE.open("a", encoding="utf-8") as file:
        file.write(f"{date};{category};{amount:.2f};{note}\n")

    print(
        f"added: {date} {category} "
        f"{amount:.2f} ({note})"
    )


def read_expenses():
    expenses = []

    if not FILE.exists():
        return expenses

    with FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            date, category, amount, note = line.split(";", 3)

            expenses.append({
                "date": date,
                "category": category,
                "amount": float(amount),
                "note": note
            })

    return expenses


def show_list():
    expenses = read_expenses()

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


def make_report():
    expenses = read_expenses()

    if not expenses:
        print("No expenses.")
        return

    total = sum(e["amount"] for e in expenses)

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category] = {
                "count": 0,
                "total": 0
            }

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

        if date not in days:
            days[date] = 0

        days[date] += expense["amount"]

    top_day = max(days, key=days.get)

    most_expensive = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    average = total / len(days)

    lines = []

    lines.append(
        f"Expenses report for {NAME} ({GROUP})"
    )
    lines.append(
        f"Period: {expenses[0]['date']} .. {expenses[-1]['date']}"
    )
    lines.append(
        f"Records: {len(expenses)}"
    )
    lines.append("")

    lines.append(
        f"{'category':<12}"
        f"{'count':>7}"
        f"{'total':>12}"
        f"{'share':>9}"
        f"  chart"
    )

    lines.append("-" * 55)

    for category, data in categories:
        share = data["total"] / total * 100
        chart = "#" * round(share / 5)

        lines.append(
            f"{category:<12}"
            f"{data['count']:>7}"
            f"{data['total']:>12.2f}"
            f"{share:>8.1f}%"
            f"  {chart}"
        )

    lines.append("-" * 55)

    lines.append(
        f"{'total':<12}"
        f"{len(expenses):>7}"
        f"{total:>12.2f}"
        f"{100:>8.1f}%"
    )

    lines.append("")

    lines.append(
        f"Top day: {top_day} ({days[top_day]:.2f})"
    )

    lines.append(
        f"Most expensive: "
        f"{most_expensive['category']} "
        f"{most_expensive['amount']:.2f} "
        f"({most_expensive['note']})"
    )

    lines.append(
        f"Average per day: {average:.2f}"
    )

    result = "\n".join(lines)

    REPORTS.mkdir(exist_ok=True)
    REPORT.write_text(result, encoding="utf-8")

    print(result)
    print()
    print(f"report saved to: {REPORT}")


def main():
    args = sys.argv[1:]

    if not args:
        usage()
        return

    if args[0] == "add":
        add_expense(args)

    elif args[0] == "list":
        show_list()

    elif args[0] == "report":
        make_report()

    else:
        print(f"error: unknown command {args[0]}")
        usage()


main()