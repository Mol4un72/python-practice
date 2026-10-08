from pathlib import Path


BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
REPORTS = BASE / "reports"
BACKUPS = BASE / "backups"


print("cwd:", Path.cwd())
print("script:", Path(__file__).resolve())
print("script dir:", BASE)
print("home:", Path.home())


DATA.mkdir(exist_ok=True)
REPORTS.mkdir(exist_ok=True)
BACKUPS.mkdir(exist_ok=True)


profile = DATA / "profile.txt"

profile.write_text(
    "name: Nazar\n"
    "surname: Tarasiuk\n"
    "group: I-23\n"
    "year: 2008\n"
    "language: Python\n",
    encoding="utf-8"
)


print()
print("profile path:", profile.resolve())
print("relative:", profile.relative_to(BASE))
print("name:", profile.name)
print("stem:", profile.stem)
print("suffix:", profile.suffix)
print("parent:", profile.parent.name)
print("size:", profile.stat().st_size, "bytes")


print()
print("project tree:")

for directory in [BASE, DATA, REPORTS, BACKUPS]:
    print("  " * (len(directory.relative_to(BASE).parts)) + directory.name + "/")

    if directory.exists():
        for file in directory.iterdir():
            if file.is_file():
                print(
                    "  " * (len(directory.relative_to(BASE).parts) + 1)
                    + file.name
                )