# File Size Analyzer Utilities

This folder contains utilities focused on inspecting file and directory sizes.
The tools are designed to answer simple but common questions:

- Where is disk space going?
- Which files are unexpectedly large?
- How big is a directory in practical terms?

These scripts favor direct filesystem inspection over abstractions.
They are intended for local analysis, cleanup preparation, or quick audits.

## Included tools

- analyzer.py  
  Core size scanner for a directory.

- largest_files.py  
  Identifies the largest files within a directory.

- directory_summary.py  
  Produces a size breakdown of immediate subdirectories.

## Design notes

- Only filesystem reads, no modifications
- Sizes are calculated explicitly, not estimated
- Output is minimal and structured
- Errors are handled quietly where expected
