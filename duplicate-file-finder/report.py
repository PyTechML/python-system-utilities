# Duplicate File Finder — reporting
# Presents duplicate file groups in a readable structure.

from pathlib import Path
from finder import find_duplicates


base = Path(input("Directory path: ").strip())

if not base.is_dir():
    print("Invalid directory")
else:
    duplicates = find_duplicates(base)

    if not duplicates:
        print("No duplicates found")
    else:
        for index, files in enumerate(duplicates.values(), start=1):
            print(f"\nGroup {index}")
            for file in files:
                print(f"  {file}")
        print(f"\nTotal duplicate groups: {len(duplicates)}")
        print(f"Total files: {sum(len(files) for files in duplicates.values())}")
        print(f"Total duplicate files: {sum(len(files) - 1 for files in duplicates.values())}")
