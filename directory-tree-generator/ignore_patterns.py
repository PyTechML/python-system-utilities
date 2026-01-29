# Directory Tree Generator — ignore patterns
# Prints directory structure while skipping specified names.

from pathlib import Path


def should_ignore(path: Path, ignore: set[str]) -> bool:
    return path.name in ignore


def print_tree(base: Path, ignore: set[str], prefix: str = "") -> int:
    count = 0
    skipped = 0

    for item in sorted(base.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
        if should_ignore(item, ignore):
            skipped += 1
            continue

        print(f"{prefix}{item.name}")
        count += 1

        if item.is_dir():
            sub_count, sub_skipped = print_tree(item, ignore, prefix + "    ")
            count += sub_count
            skipped += sub_skipped

    return count, skipped


base = Path(input("Directory path: ").strip())
raw = input("Ignore names (comma separated): ").strip()
ignore_set = {name.strip() for name in raw.split(",") if name.strip()}

if not base.is_dir():
    print("Invalid directory")
else:
    print(f"\nScanning directory: {base}")
    print(f"Ignoring: {', '.join(ignore_set) if ignore_set else 'none'}\n")

    listed, skipped = print_tree(base, ignore_set)

    print(f"\nScan completed — {listed} items listed, {skipped} skipped")
