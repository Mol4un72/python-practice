from pathlib import Path
from datetime import datetime


BASE = Path(__file__).resolve().parent
LOG = BASE / "data" / "runs.log"

NAME = "Nazar Tarasiuk"


def count_runs(path):
    if not path.exists():
        return 0

    with path.open("r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


def add_run(path, number):
    path.parent.mkdir(exist_ok=True)

    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with path.open("a", encoding="utf-8") as file:
        file.write(f"{number};{stamp};{NAME}\n")


def show_history(path, last=3):
    with path.open("r", encoding="utf-8") as file:
        records = [line.strip() for line in file if line.strip()]

    print("runs so far:", len(records))
    print("last runs:")

    for record in records[-last:]:
        number, date, name = record.split(";", 2)
        print(f"#{number}  {date}  {name}")

    first = records[0].split(";", 2)
    print("first run was at", first[1])


def main():
    number = count_runs(LOG) + 1

    add_run(LOG, number)

    print(f"Hello, {NAME}! This is run number {number}.")

    if number == 1:
        print("runs.log was just created.")

    show_history(LOG)


main()