# Task Timer — session log
# Displays all recorded task timer entries.

from pathlib import Path

LOG_FILE = Path("task_log.txt")

if not LOG_FILE.exists():
    print("No task sessions recorded")
else:
    print("\nRecorded task sessions:\n")

    with LOG_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            timestamp, task, action = line.strip().split(",", 2)
            print(f"{timestamp} | {task} | {action}")

    print("\nLog display completed")
