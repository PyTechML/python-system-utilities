# File Renamer — controlled rename
# Applies renaming only after explicit user confirmation.

from pathlib import Path


def rename_files(directory: Path, prefix: str) -> int:
    renamed = 0

    for file in directory.iterdir():
        if not file.is_file():
            continue

        target = directory / f"{prefix}{file.name}"

        if target.exists():
            print(f"Skipped (exists): {target.name}")
            continue

        file.rename(target)
        renamed += 1
        print(f"Renamed: {file.name} -> {target.name}")

    return renamed


base = Path(input("Directory path: ").strip())
prefix = input("Prefix to add: ").strip()

if not base.is_dir():
    print("Invalid directory")
else:
    confirm = input("Apply changes? (y/n): ").strip().lower()
    if confirm != "y":
        print("Operation cancelled")
    else:
        print(f"\nRenaming files in: {base}\n")
        total = rename_files(base, prefix)
        print(f"\nRename completed — {total} files renamed")
