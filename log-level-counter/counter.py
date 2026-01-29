# Log Level Counter — level aggregation
# Counts occurrences of common log levels in a file.

from pathlib import Path


LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")


def count_levels(log_file: Path) -> dict[str, int]:
    counts = {level: 0 for level in LEVELS}

    with log_file.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for level in LEVELS:
                if level in line:
                    counts[level] += 1
                    break

    return counts


path = Path(input("Log file path: ").strip())

if not path.is_file():
    print("Invalid log file")
else:
    print(f"\nAnalyzing log file: {path}\n")

    result = count_levels(path)
    total = sum(result.values())

    for level, count in result.items():
        print(f"{level}: {count}")

    print(f"\nAnalysis completed — {total} matching entries found")
