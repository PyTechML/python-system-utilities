# Task Timer — time summary
# Calculates total time spent per task based on start/stop pairs.

from datetime import datetime
from pathlib import Path
from collections import defaultdict

LOG_FILE = Path("task_log.txt")


def parse_time(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


sessions = defaultdict(list)

if not LOG_FILE.exists():
    print("No task data available")
else:
    with LOG_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            timestamp, task, action = line.strip().split(",", 2)
            sessions[task].append((parse_time(timestamp), action))

    print("\nTask time summary:\n")

    for task, events in sessions.items():
        events.sort()
        total = 0
        start_time = None

        for time, action in events:
            if action == "start":
                start_time = time
            elif action == "stop" and start_time:
                total += (time - start_time).total_seconds()
                start_time = None

        minutes = int(total // 60)
        seconds = int(total % 60)

        print(f"{task}: {minutes}m {seconds}s")

    print("\nSummary completed")
