# Port Checker — range scan
# Scans a range of TCP ports and reports which are open.

import socket


def scan(host: str, start: int, end: int, timeout: float = 0.5) -> list[int]:
    open_ports = []

    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((host, port)) == 0:
                open_ports.append(port)

    return open_ports


host = input("Host (default: localhost): ").strip() or "localhost"
start = int(input("Start port: ").strip())
end = int(input("End port: ").strip())

print(f"\nScanning ports {start}-{end} on {host}\n")

open_ports = scan(host, start, end)

if not open_ports:
    print("No open ports found")
else:
    print("Open ports:")
    for port in open_ports:
        print(f"  {port}")

print("\nScan completed")
