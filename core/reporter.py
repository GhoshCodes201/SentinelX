def generate(target, ports, headers, sqli, xss, admins):
    """Write a simple report to report.txt (placeholder)."""
    lines = []
    lines.append(f"Target: {target}\n")
    lines.append(f"Open ports: {ports}\n")
    lines.append(f"Headers: {headers}\n")
    lines.append(f"SQLi: {sqli}\n")
    lines.append(f"XSS: {xss}\n")
    lines.append(f"Admin panels: {admins}\n")
    with open('report.txt', 'w') as f:
        f.writelines(lines)
def generate(target, ports, headers, sqli, xss, admins):
    lines = []
    lines.append(f"Report for: {target}\n")
    lines.append("Ports:\n")
    for p in ports:
        lines.append(f" - {p}\n")
    lines.append("\nHeaders:\n")
    for k, v in headers.items():
        lines.append(f" - {k}: {v}\n")
    lines.append("\nSQLi Vulnerable: " + ("Yes" if sqli else "No") + "\n")
    lines.append("XSS Vulnerable: " + ("Yes" if xss else "No") + "\n")
    lines.append("\nPotential admin pages:\n")
    for a in admins:
        lines.append(f" - {a}\n")

    with open('report.txt', 'w') as fh:
        fh.writelines(lines)
def generate(target, ports, headers, sqli, xss, admins):
    with open("report.txt","w") as f:
        f.write(f"TARGET : {target}\n")
        f.write(f"Open Ports : {ports}\n")
        f.write(f"Missing Headers : {headers}\n")
        f.write(f"SQLi : {sqli}\n")
        f.write(f"XSS : {xss}\n")
        f.write(f"Admin Panels : {admins}\n")
