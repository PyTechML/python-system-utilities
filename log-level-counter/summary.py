# Log Level Counter — multi-file summary
# Produces a combined level summary across log files in a directory.

from pathlib import Path


LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")


def summarize(directory: Path) -> dict[str, int]:
    totals = {level: 0 for level in LEVELS}

    for log in directory.iterdir():
        if not log.is_file():
            continue

        with log.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                for level in LEVELS:
                    if level in line:
                        totals[level] += 1
                        break

    return totals


base = Path(input("Log directory path: ").strip())

if not base.is_dir():
    print("Invalid directory")
else:
    print(f"\nSummarizing logs in: {base}\n")

    result = summarize(base)
    total = sum(result.values())

    for level, count in result.items():
        print(f"{level}: {count}")

    print(f"\nSummary completed — {total} matching entries found")
