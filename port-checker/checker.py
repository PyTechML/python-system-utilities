# Port Checker — single port check
# Verifies whether a TCP port is reachable on a given host.

import socket


def is_open(host: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


host = input("Host (default: localhost): ").strip() or "localhost"
port = int(input("Port: ").strip())

print(f"\nChecking {host}:{port}\n")

open_ = is_open(host, port)

if open_:
    print(f"Port {port} is open")
else:
    print(f"Port {port} is closed or unreachable")

print("\nCheck completed")
