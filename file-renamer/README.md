# File Renamer Utilities

This folder contains utilities for renaming files in a controlled and
predictable way.

Renaming is treated as a potentially destructive operation. For that reason,
every script here either previews changes first or reports actions explicitly.

These tools are intended for cleanup tasks, consistency enforcement, or
preparation before further processing.

## Included tools

- renamer.py  
  Core renaming utility with explicit confirmation.

- pattern_rename.py  
  Renames files using a simple pattern-based rule.

- preview.py  
  Displays rename operations without applying them.

## Design notes

- No recursive renaming unless stated
- No silent overwrites
- All actions are reported to the terminal
- Preview-first mindset
