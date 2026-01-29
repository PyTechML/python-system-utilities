# Port Checker Utilities

This folder contains utilities for inspecting TCP port availability on a local
or remote host.

These tools are intended for debugging services, validating deployments, or
quickly confirming whether a process is reachable.

All checks are non-intrusive. No ports are opened or modified.

## Included tools

- checker.py  
  Checks availability of a single TCP port.

- range_scan.py  
  Scans a range of ports and reports open ones.

- service_probe.py  
  Attempts a lightweight connection to identify basic service response.

## Design notes

- Uses standard socket operations
- Explicit timeouts to avoid hanging
- Clear reporting of checked ports
- Output focuses on results, not theory
