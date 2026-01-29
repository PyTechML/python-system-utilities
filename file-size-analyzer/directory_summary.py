# File Size Analyzer — directory summary
# Provides size totals for immediate subdirectories.

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


base = Path(input("Directory path: ").strip())

if not base.is_dir():
    print("Invalid directory")
else:
    for sub in base.iterdir():
        if sub.is_dir():
            size = directory_size(sub)
            print(f"{sub.name}: {format_size(size)}")
