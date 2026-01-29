# Task Timer Utilities

This folder contains small utilities for tracking time spent on tasks.
The focus is on simplicity, persistence, and clear reporting.

These tools are designed for personal productivity, lightweight tracking,
or quick audits of time allocation during development work.

All data is stored locally in plain text files.

## Included tools

- timer.py  
  Starts and stops a timer for a named task.

- session_log.py  
  Displays recorded task sessions.

- report.py  
  Produces a summary of time spent per task.

## Design notes

- Time is tracked explicitly, not inferred
- Sessions are append-only
- No background processes
- Output explains exactly what was recorded
