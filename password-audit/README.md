# Password Audit Utilities

This folder contains utilities for evaluating password strength and policy
compliance.

The tools here are designed for validation and auditing purposes only. They do
not store, transmit, or log passwords in any form.

These scripts are useful when enforcing minimum security standards or validating
inputs before acceptance.

## Included tools

- audit.py  
  Performs a full password audit against common security rules.

- policy_check.py  
  Validates a password against a configurable policy.

- strength_score.py  
  Produces a numeric strength score with clear interpretation.

## Design notes

- No password persistence
- No external dependencies
- Clear pass/fail reasoning
- Output explains results, not theory
