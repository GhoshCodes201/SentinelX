def scan_sqli(url):
    """Placeholder SQLi scanner: always reports not vulnerable."""
    return {"vulnerable": False, "details": "stub - no scan performed"}
def scan_sqli(url):
    # Minimal stub: indicate no SQLi found
    return False
import requests

payload = "' OR '1'='1"

def scan_sqli(url):
    test_url = url + payload
    r = requests.get(test_url)
    if "sql" in r.text.lower() or "mysql" in r.text.lower():
        return True
    return False
