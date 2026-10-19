from pathlib import Path
import sys


def usage():
    print("usage: python3 task2.py [--force] <source> <destination>")


def main():
    args = sys.argv[1:]
    force = False

    if args and args[0] == "--force":
        force = True
        args = args[1:]

    if len(args) != 2:
        usage()
        return 2

    source = Path(args[0])
    destination = Path(args[1])

    try:
        if not source.exists():
            print(f"error: source {source} not found")
            return 1

        if source.is_dir():
            print(f"error: source {source} is a directory, not a file")
            return 1

        if not source.is_file():
            print(f"error: source {source} is not a regular file")
            return 1

        if not destination.parent.is_dir():
            print(f"error: destination folder {destination.parent} not found")
            return 1

        if destination.exists() and destination.is_dir():
            print(f"error: destination {destination} is a directory, not a file")
            return 1

        if destination.exists() and source.samefile(destination):
            print("error: source and destination are the same file")
            return 1

        if destination.exists() and not force:
            print(
                f"error: {destination} already exists, "
                "use --force to overwrite"
            )
            return 1

        # Перевіряємо, що джерело є текстом у UTF-8.
        content = source.read_text(encoding="utf-8")

        destination.write_text(content, encoding="utf-8")

        print(f"copied: {source} -> {destination}")
        return 0

    except UnicodeDecodeError:
        print(f"error: source {source} is not a UTF-8 text file")
        return 1

    except OSError as error:
        print(f"error: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())