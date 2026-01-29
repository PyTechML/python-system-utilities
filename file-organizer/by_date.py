# File Organizer — date based grouping
# Organizes files using last modified year and month.

from pathlib import Path
from datetime import datetime


def organize_by_date(directory: Path) -> None:
    if not directory.is_dir():
        print("Invalid directory")
        return

    for file in directory.iterdir():
        if not file.is_file():
            continue

        timestamp = datetime.fromtimestamp(file.stat().st_mtime)
        year = str(timestamp.year)
        month = f"{timestamp.month:02d}"

        target = directory / year / month
        target.mkdir(parents=True, exist_ok=True)

        file.rename(target / file.name)

    print("Date-based organization completed")


directory = Path(input("Directory: ").strip())
organize_by_date(directory)
