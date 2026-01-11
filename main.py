import os
import sys

ROOT = os.path.dirname(__file__)
if ROOT not in sys.path:
	sys.path.insert(0, ROOT)

try:
	from banner import show_banner
	from core.port_scanner import scan_ports
	from core.header_scanner import scan_headers
	from core.sqli_scanner import scan_sqli
	from core.xss_scanner import scan_xss
	from core.admin_finder import find_admin
	from core.reporter import generate
except Exception:
	
	from importlib import import_module
	show_banner = import_module('banner').show_banner
	scan_ports = import_module('core.port_scanner').scan_ports
	scan_headers = import_module('core.header_scanner').scan_headers
	scan_sqli = import_module('core.sqli_scanner').scan_sqli
	scan_xss = import_module('core.xss_scanner').scan_xss
	find_admin = import_module('core.admin_finder').find_admin
	generate = import_module('core.reporter').generate

show_banner()
target = input("Enter Target Domain (example.com): ")

ports = scan_ports(target)
headers = scan_headers("http://"+target)
sqli = scan_sqli("http://"+target+"/?id=1")
xss = scan_xss("http://"+target+"/?q=")
admins = find_admin("http://"+target)

generate(target, ports, headers, sqli, xss, admins)

print("\nReport saved as report.txt")
