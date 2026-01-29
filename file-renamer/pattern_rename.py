# File Renamer — pattern based
# Renames files using a simple find-and-replace rule.

from pathlib import Path


def pattern_rename(directory: Path, find: str, replace: str) -> int:
    renamed = 0

    for file in directory.iterdir():
        if not file.is_file():
            continue

        if find not in file.name:
            continue

        new_name = file.name.replace(find, replace)
        target = directory / new_name

        if target.exists():
            print(f"Skipped (exists): {new_name}")
            continue

        file.rename(target)
        renamed += 1
        print(f"Renamed: {file.name} -> {new_name}")

    return renamed


base = Path(input("Directory path: ").strip())
find = input("Find text: ").strip()
replace = input("Replace with: ").strip()

if not base.is_dir():
    print("Invalid directory")
else:
    print(f"\nApplying pattern rename in: {base}\n")
    total = pattern_rename(base, find, replace)
    print(f"\nRename completed — {total} files renamed")
