# Port Checker — service probe
# Attempts a minimal connection to observe basic service behavior.

import socket


def probe(host: str, port: int, timeout: float = 1.0) -> str:
    try:
        with socket.create_connection((host, port), timeout=timeout) as s:
            s.sendall(b"\n")
            data = s.recv(64)
            return data.decode(errors="ignore").strip()
    except Exception:
        return ""


host = input("Host (default: localhost): ").strip() or "localhost"
port = int(input("Port: ").strip())

print(f"\nProbing service at {host}:{port}\n")

response = probe(host, port)

if response:
    print("Service responded:")
    print(response)
else:
    print("No response received")

print("\nProbe completed")
