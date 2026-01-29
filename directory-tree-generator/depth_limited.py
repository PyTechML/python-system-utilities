# Directory Tree Generator — depth limited
# Prints directory structure up to a defined depth level.

from pathlib import Path


def print_tree(base: Path, depth: int, current: int = 0, prefix: str = "") -> int:
    if current > depth:
        return 0

    count = 0

    for item in sorted(base.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
        print(f"{prefix}{item.name}")
        count += 1

        if item.is_dir():
            count += print_tree(item, depth, current + 1, prefix + "    ")

    return count


base = Path(input("Directory path: ").strip())
max_depth = int(input("Max depth: ").strip())

if not base.is_dir():
    print("Invalid directory")
else:
    print(f"\nScanning up to depth {max_depth} in: {base}\n")
    total = print_tree(base, max_depth)
    print(f"\nScan completed — {total} items listed")
