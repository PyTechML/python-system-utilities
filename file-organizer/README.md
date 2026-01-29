# File Organizer Utilities

This directory contains small, focused utilities for organizing files on disk.
Each script is designed to be used independently, depending on how files need
to be grouped or inspected before moving.

The tools here are intentionally simple and predictable. They favor safety,
explicit input, and readable behavior over aggressive automation.

## Included tools

- organizer.py  
  Core entry point. Organizes files by extension in a target directory.

- by_extension.py  
  Groups files into folders based strictly on file extensions.

- by_date.py  
  Organizes files using last modified date (year/month structure).

- dry_run.py  
  Simulates organization without modifying the filesystem.

## Design notes

- Directories are never modified unless explicitly required
- Existing folders are reused when possible
- Failures are handled quietly when expected
- No recursive behavior unless stated

These scripts are meant to be used as internal tools or extended further
depending on system needs.
