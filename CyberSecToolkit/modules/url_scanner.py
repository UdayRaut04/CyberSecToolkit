import tkinter as tk
from tkinter import messagebox
import re
import validators
import requests

# Optional: Get a free API key from https://virustotal.com
VIRUSTOTAL_API_KEY = ""  # Add your API key here

def is_suspicious_url(url):
    if not validators.url(url):
        return True, "Invalid URL format."

    suspicious_patterns = [
        r"\d{1,3}(?:\.\d{1,3}){3}",  # IP in URL
        r"(login|verify|update|secure)\w*\.",  # phishing keywords
        r"@.*",  # @ in URL (obfuscation)
        r"https?:\/\/.*\..*\.com"  # double domain
    ]
    for pattern in suspicious_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            return True, f"Suspicious pattern detected: {pattern}"

    return False, "Looks okay (basic check)"

def scan_virustotal(url):
    if not VIRUSTOTAL_API_KEY:
        return "VirusTotal API key not set."

    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    params = {"url": url}
    response = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data=params)

    if response.status_code == 200:
        data = response.json()
        scan_id = data["data"]["id"]
        report = requests.get(f"https://www.virustotal.com/api/v3/analyses/{scan_id}", headers=headers)
        result = report.json()
        stats = result["data"]["attributes"]["stats"]
        malicious = stats.get("malicious", 0)
        return f"VirusTotal: {malicious} detections"
    else:
        return f"Error from VirusTotal: {response.status_code}"

def launch_url_scanner():
    win = tk.Toplevel()
    win.title("🦠 Malicious URL Scanner")
    win.geometry("400x300")
    win.config(bg="#1c1c1c")

    status_label = tk.Label(win, text="", bg="#1c1c1c", fg="white", wraplength=350)
    status_label.pack(pady=10)

    tk.Label(win, text="Enter URL to scan:", bg="#1c1c1c", fg="white").pack(pady=5)
    url_entry = tk.Entry(win, width=40)
    url_entry.pack(pady=5)

    def check_url():
        url = url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        suspicious, reason = is_suspicious_url(url)
        result_msg = f"🔍 Basic Scan: {'❌ Suspicious' if suspicious else '✅ Clean'}\nReason: {reason}"

        if VIRUSTOTAL_API_KEY:
            vt_result = scan_virustotal(url)
            result_msg += f"\n\n🛡️ {vt_result}"
        else:
            result_msg += "\n\n🛡️ VirusTotal not used (no API key set)."

        status_label.config(text=result_msg, fg="lightgreen" if not suspicious else "orange")

    tk.Button(win, text="Scan URL", command=check_url, bg="#444", fg="white").pack(pady=15)
