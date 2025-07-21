import tkinter as tk
from tkinter import messagebox
import socket
import threading
from datetime import datetime

def scan_ports(host, start, end, result_label):
    open_ports = []
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        result_label.config(text="❌ Invalid hostname.")
        return

    result_label.config(text="🔍 Scanning... please wait.")

    def scan():
        t1 = datetime.now()
        for port in range(start, end + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        t2 = datetime.now()
        duration = str(t2 - t1)

        if open_ports:
            result_label.config(fg="lightgreen", text=f"✅ Open ports: {open_ports}\n⏱ Time: {duration}")
        else:
            result_label.config(fg="orange", text=f"No open ports found.\n⏱ Time: {duration}")

    threading.Thread(target=scan).start()

def launch_port_scanner():
    window = tk.Toplevel()
    window.title("🌐 Port Scanner")
    window.geometry("400x400")
    window.config(bg="#2c2c2c")

    tk.Label(window, text="Target Host/IP:", bg="#2c2c2c", fg="white").pack(pady=5)
    host_entry = tk.Entry(window, width=30)
    host_entry.pack()

    tk.Label(window, text="Start Port:", bg="#2c2c2c", fg="white").pack(pady=5)
    start_entry = tk.Entry(window, width=10)
    start_entry.pack()

    tk.Label(window, text="End Port:", bg="#2c2c2c", fg="white").pack(pady=5)
    end_entry = tk.Entry(window, width=10)
    end_entry.pack()

    result = tk.Label(window, text="", bg="#2c2c2c", fg="white", wraplength=350)
    result.pack(pady=15)

    def start_scan():
        host = host_entry.get()
        try:
            start_port = int(start_entry.get())
            end_port = int(end_entry.get())
            if start_port > end_port:
                raise ValueError
        except ValueError:
            result.config(fg="red", text="❌ Invalid port range.")
            return
        scan_ports(host, start_port, end_port, result)

    tk.Button(window, text="Scan", command=start_scan, bg="#444", fg="white").pack(pady=10)
