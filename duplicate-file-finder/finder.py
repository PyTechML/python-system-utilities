# Duplicate File Finder — core scanner
# Identifies files with identical content using SHA-256 hashes.

from pathlib import Path
from collections import defaultdict
from hash_utils import file_hash


def find_duplicates(directory: Path):
    hashes = defaultdict(list)

    for item in directory.rglob("*"):
        if not item.is_file():
            continue

        try:
            digest = file_hash(item)
            hashes[digest].append(item)
        except OSError:
            continue

    return {h: files for h, files in hashes.items() if len(files) > 1}


base = Path(input("Directory path: ").strip())

if not base.is_dir():
    print("Invalid directory")
else:
    duplicates = find_duplicates(base)
    print(f"Duplicate groups found: {len(duplicates)}")
    for group in duplicates.values():
        print("Duplicate group:")
        for file in group:
            print(f" - {file}")
    print("Scan complete.")


