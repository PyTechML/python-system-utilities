# File Organizer — core dispatcher
# Handles basic directory validation and routes files to extension-based folders.

from pathlib import Path


def organize(directory: Path) -> None:
    if not directory.exists() or not directory.is_dir():
        print("Invalid directory path")
        return

    for item in directory.iterdir():
        if item.is_dir():
            continue

        extension = item.suffix.lower().strip(".") or "no_extension"
        target_dir = directory / extension

        target_dir.mkdir(exist_ok=True)
        item.rename(target_dir / item.name)

    print("Organization completed")


path_input = input("Target directory path: ").strip()
organize(Path(path_input))
