# Environment Variable Validator Utilities

This folder contains utilities for validating environment configuration files.
The focus is on detecting missing, empty, or inconsistent configuration values
before an application is run.

These scripts are intended for pre-run checks, local debugging, or CI sanity
validation.

All tools are read-only and safe by default.

## Included tools

- validator.py  
  Core validator for required environment keys.

- required_keys.py  
  Compares an environment file against a required key list.

- sample_compare.py  
  Compares a `.env` file against a sample template.

## Design notes

- Line-based parsing
- No dependency on external libraries
- Explicit reporting of missing or invalid entries
- No assumptions about runtime environment
