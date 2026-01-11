def scan_xss(url):
    """Placeholder XSS scanner: always reports not vulnerable."""
    return {"vulnerable": False, "details": "stub - no scan performed"}
def scan_xss(url):
    # Minimal stub: indicate no XSS found
    return False
import requests

payload = "<script>alert(1)</script>"

def scan_xss(url):
    r = requests.get(url+payload)
    return payload in r.text
