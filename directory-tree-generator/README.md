# Directory Tree Generator Utilities

This folder contains utilities for inspecting and visualizing directory
structures in a predictable, text-based format.

These tools are useful when auditing large projects, documenting structures,
or quickly understanding how files are organized on disk.

The scripts generate output only. No filesystem changes are made.

## Included tools

- tree.py  
  Prints a full directory tree.

- depth_limited.py  
  Prints a directory tree up to a specified depth.

- ignore_patterns.py  
  Prints a directory tree while ignoring specific folders or file patterns.

## Design notes

- Read-only operations
- Output is explicit and structured
- Each run reports what was scanned and what was skipped
- No recursive surprises
