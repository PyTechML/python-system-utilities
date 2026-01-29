# Task Timer — start/stop session
# Records time spent on a named task.

from datetime import datetime
from pathlib import Path

LOG_FILE = Path("task_log.txt")


def log(entry: str) -> None:
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(entry + "\n")


task = input("Task name: ").strip()
action = input("Action (start/stop): ").strip().lower()

timestamp = datetime.now().isoformat(timespec="seconds")

if action not in {"start", "stop"}:
    print("Invalid action")
else:
    log(f"{timestamp},{task},{action}")
    print(f"{action.capitalize()} recorded for task '{task}'")
