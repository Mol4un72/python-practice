from pathlib import Path
import sys


def check_file(path):
    try:
        with path.open("r", encoding="utf-8") as file:
            content = file.read()

        if not content:
            raise ValueError("file is empty")

        lines = content.splitlines()

        print(
            f"ok:    {path}: {len(lines)} lines, "
            f"first: {lines[0]}"
        )
        return True

    except FileNotFoundError as error:
        print(
            f"error: {path}: file not found "
            f"({type(error).__name__})"
        )

    except IsADirectoryError as error:
        print(
            f"error: {path}: is a directory "
            f"({type(error).__name__})"
        )

    except UnicodeDecodeError as error:
        print(
            f"error: {path}: not a UTF-8 text file "
            f"({type(error).__name__})"
        )

    except ValueError as error:
        print(
            f"error: {path}: {error} "
            f"({type(error).__name__})"
        )

    except OSError as error:
        print(
            f"error: {path}: {error} "
            f"({type(error).__name__})"
        )

    return False


def main():
    paths = sys.argv[1:]

    if not paths:
        print("usage: python3 task1.py <path> [<path> ...]")
        return 2

    checked = 0
    failed = 0

    for name in paths:
        checked += 1

        if not check_file(Path(name)):
            failed += 1

    print(f"checked {checked}, failed {failed}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())