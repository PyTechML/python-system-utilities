# File Size Analyzer — largest file inspection
# Lists the largest files within a directory tree.

from pathlib import Path


def largest_files(path: Path, limit: int = 5):
    files = []

    for item in path.rglob("*"):
        if item.is_file():
            files.append((item, item.stat().st_size))

    files.sort(key=lambda x: x[1], reverse=True)
    return files[:limit]


def format_size(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"


directory = Path(input("Directory path: ").strip())
count = int(input("How many files to list: ").strip() or 5)

if not directory.is_dir():
    print("Invalid directory")
else:
    results = largest_files(directory, count)
    for file, size in results:
        print(f"{file} -> {format_size(size)}")
