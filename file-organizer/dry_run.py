# File Organizer — dry run mode
# Shows how files would be organized without making changes.

from pathlib import Path


def simulate(directory: Path) -> None:
    if not directory.is_dir():
        print("Invalid directory")
        return

    for file in directory.iterdir():
        if not file.is_file():
            continue

        ext = file.suffix.lower().strip(".") or "no_extension"
        target = directory / ext / file.name

        print(f"{file.name} -> {target}")

    print("Dry run completed")


directory = Path(input("Directory: ").strip())
simulate(directory)
