import socket
import sys
import time
import threading

usage = "python port_scanner.py TARGET START_PORT END_PORT"

print("-" * 70)
print("Python Port Scanner")
print("-" * 70)

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

# Check if the target is a valid IP address or a hostname
target = sys.argv[1]
try:
    # Try to resolve the hostname to an IP address
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    # If it's not a valid domain name, check if it's a valid IP address
    try:
        socket.inet_aton(target)
        target_ip = target  # Valid IP address, don't need to resolve
    except socket.error:
        print("Invalid IP address or domain name.")
        sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target:", target_ip)

def scan_port(port):
    print( port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target_ip, port))
    if not conn:
        print("Port {} is OPEN".format(port))
    s.close()

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.daemon = True
    thread.start()
