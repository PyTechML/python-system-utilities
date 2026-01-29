# Directory Tree Generator — full tree
# Prints a complete directory structure starting from a given path.

from pathlib import Path


def print_tree(base: Path, prefix: str = "") -> int:
    count = 0

    for item in sorted(base.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
        print(f"{prefix}{item.name}")
        count += 1

        if item.is_dir():
            count += print_tree(item, prefix + "    ")

    return count


base = Path(input("Directory path: ").strip())

if not base.is_dir():
    print("Invalid directory")
else:
    print(f"\nScanning directory: {base}\n")
    total = print_tree(base)
    print(f"\nScan completed — {total} items listed")
