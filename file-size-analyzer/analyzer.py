# File Size Analyzer — directory scanner
# Calculates total size of all files inside a directory.

from pathlib import Path


def directory_size(path: Path) -> int:
    total = 0

    for item in path.rglob("*"):
        if item.is_file():
            total += item.stat().st_size

    return total


def format_size(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"


directory = Path(input("Directory path: ").strip())

if not directory.is_dir():
    print("Invalid directory")
else:
    size = directory_size(directory)
    print("Total size:", format_size(size))
