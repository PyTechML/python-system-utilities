# Duplicate File Finder Utilities

This folder contains utilities for detecting duplicate files based on content,
not filenames.

The approach relies on hashing file contents to ensure correctness. These tools
are intended for disk cleanup analysis, audits, or verification tasks where
accuracy matters more than speed.

Scripts are designed to be safe by default. No files are deleted or modified.

## Included tools

- finder.py  
  Core duplicate detection logic using content hashes.

- hash_utils.py  
  Shared helpers for hashing files efficiently.

- report.py  
  Formats and presents duplicate groups in a readable way.

## Design notes

- Hash-based comparison, not name-based
- Files are read in chunks to avoid memory issues
- No automatic deletion or destructive behavior
- Output favors clarity over verbosity
