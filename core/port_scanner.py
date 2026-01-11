def scan_ports(target):
    """Return a small list of common ports as a placeholder."""
    # Minimal stub: pretend ports 80 and 443 are open
    return [80, 443]
def scan_ports(target):
    # Minimal stub: return common open ports for quick demo
    try:
        host = str(target)
    except Exception:
        host = target
    return [80, 443]
import socket

def scan_ports(target):
    open_ports = []
    for port in [21,22,23,25,53,80,110,443,3306]:
        s = socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((target, port)) == 0:
            open_ports.append(port)
        s.close()
    return open_ports
