def find_admin(url):
    """Return a list with a common /admin path as a placeholder."""
    if not url.startswith("http"):
        url = "http://" + url
    return [url.rstrip('/') + '/admin']
def find_admin(url):
    # Minimal stub: return common admin paths (no network checks)
    return [url.rstrip('/') + '/admin', url.rstrip('/') + '/administrator']
import requests

paths = ["/admin","/administrator","/admin/login.php","/wp-admin"]

def find_admin(url):
    found=[]
    for p in paths:
        r=requests.get(url+p)
        if r.status_code==200:
            found.append(url+p)
    return found
