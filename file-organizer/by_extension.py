# File Organizer — extension based grouping
# Focuses purely on separating files by their extensions.

from pathlib import Path


def group_by_extension(directory: Path) -> None:
    if not directory.is_dir():
        print("Invalid directory")
        return

    files = [f for f in directory.iterdir() if f.is_file()]

    for file in files:
        ext = file.suffix.lower().strip(".") or "no_extension"
        dest = directory / ext
        dest.mkdir(exist_ok=True)

        file.rename(dest / file.name)

    print(f"Processed {len(files)} files")


directory = Path(input("Directory: ").strip())
group_by_extension(directory)
