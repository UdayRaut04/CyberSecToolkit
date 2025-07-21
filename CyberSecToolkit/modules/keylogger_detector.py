import psutil
import tkinter as tk
from tkinter import messagebox
import os

suspicious_keywords = [
    "pynput", "keyboard", "keylogger", "pyxhook",
    "win32api", "win32console", "GetAsyncKeyState"
]

def detect_suspicious_processes():
    flagged = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = ' '.join(proc.info['cmdline'])
            for keyword in suspicious_keywords:
                if keyword.lower() in cmdline.lower():
                    flagged.append(f"PID {proc.info['pid']} - {proc.info['name']}\n{cmdline}")
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return flagged

def launch_keylogger_detector():
    win = tk.Toplevel()
    win.title("🕵️ Keylogger Detector")
    win.geometry("500x400")
    win.config(bg="#1c1c1c")

    tk.Label(win, text="🛡️ Running Keylogger Check...", fg="white", bg="#1c1c1c", font=("Arial", 12)).pack(pady=10)
    output_text = tk.Text(win, wrap=tk.WORD, bg="#1c1c1c", fg="lightgreen", height=15)
    output_text.pack(padx=10, pady=10)

    def run_detection():
        output_text.delete("1.0", tk.END)
        flagged = detect_suspicious_processes()

        if flagged:
            output_text.insert(tk.END, "⚠️ Potential Keylogger Processes Detected:\n\n")
            for item in flagged:
                output_text.insert(tk.END, f"{item}\n\n")
        else:
            output_text.insert(tk.END, "✅ No suspicious keylogger processes found.")

    tk.Button(win, text="Scan Again", command=run_detection, bg="#444", fg="white").pack(pady=10)
    run_detection()
