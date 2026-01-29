# Log Level Counter — error extraction
# Reports error and critical entries from a log file.

from pathlib import Path


ERROR_LEVELS = ("ERROR", "CRITICAL")


def extract_errors(log_file: Path) -> int:
    count = 0

    with log_file.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if any(level in line for level in ERROR_LEVELS):
                print(line.rstrip())
                count += 1

    return count


path = Path(input("Log file path: ").strip())

if not path.is_file():
    print("Invalid log file")
else:
    print(f"\nExtracting errors from: {path}\n")

    total = extract_errors(path)
    print(f"\nExtraction completed — {total} error entries found")
