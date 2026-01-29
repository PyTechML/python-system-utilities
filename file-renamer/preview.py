# File Renamer — preview mode
# Shows how files would be renamed without applying changes.

from pathlib import Path


def preview(directory: Path, prefix: str) -> int:
    count = 0

    for file in directory.iterdir():
        if not file.is_file():
            continue

        new_name = f"{prefix}{file.name}"
        print(f"{file.name} -> {new_name}")
        count += 1

    return count


base = Path(input("Directory path: ").strip())
prefix = input("Prefix to add: ").strip()

if not base.is_dir():
    print("Invalid directory")
else:
    print(f"\nPreviewing rename in: {base}\n")
    total = preview(base, prefix)
    print(f"\nPreview completed — {total} files would be renamed")
