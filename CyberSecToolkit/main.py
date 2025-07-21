from modules.password_checker import launch_password_checker
from modules.port_scanner import launch_port_scanner
from modules.file_encryptor import launch_file_encryptor
from modules.url_scanner import launch_url_scanner
from modules.keylogger_detector import launch_keylogger_detector
from modules.file_shredder import launch_file_shredder

import ttkbootstrap as tb
from ttkbootstrap import Label

import tkinter as tk
from tkinter import messagebox

# Main window setup
root = tk.Tk()
root.title("CyberSecToolkit 🛡️")
root.geometry("400x500")
root.config(bg="#020202")

# Heading
title = tk.Label(root, text="CyberSecToolkit", font=("Helvetica", 20, "bold"), bg="#020202", fg="white")
title.pack(pady=20)

# Button style helper
def create_button(text, command):
    return tk.Button(root, text=text, command=command, width=30, height=2, bg="#800080", fg="white", bd=0, activebackground="#00ffcc")

# Placeholder commands for now
def not_ready():
    messagebox.showinfo("Coming Soon", "This tool is not implemented yet.")

# Buttons for each tool
create_button("🔑 Password Strength Checker", launch_password_checker).pack(pady=10)
create_button("🌐 Port Scanner", launch_port_scanner).pack(pady=10)
create_button("🦠 Malicious URL Scanner", launch_url_scanner).pack(pady=10)
create_button("🔐 File Encryptor/Decryptor", launch_file_encryptor).pack(pady=10)
create_button("🕵️ Keylogger Detector", launch_keylogger_detector).pack(pady=10)
create_button("🗑️ Secure File Shredder", launch_file_shredder).pack(pady=10)



# ...

Label(root, text="Designed by Uday Raut with 🖤 for Cybersecurity Learners", font=("Segoe UI", 10), bootstyle="secondary").pack(side="bottom", pady=15)


# Start GUI loop
root.mainloop()
