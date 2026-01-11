def scan_headers(url):
    """Return a small dict of headers as a placeholder."""
    return {
        "Server": "nginx",
        "X-Frame-Options": "DENY",
    }
def scan_headers(url):
    # Minimal stub: return example headers
    return {
        'Server': 'nginx/1.18.0',
        'X-Powered-By': 'Python'
    }
import requests

def scan_headers(url):
    r = requests.get(url)
    missing = []

    headers = ["X-Frame-Options","Content-Security-Policy","X-XSS-Protection"]
    for h in headers:
        if h not in r.headers:
            missing.append(h)

    return missing
