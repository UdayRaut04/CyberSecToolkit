import tkinter as tk
import re

def check_strength(password):
    errors = []

    if len(password) < 8:
        errors.append("Too short (min 8 characters)")
    if not re.search(r"\d", password):
        errors.append("Missing a digit")
    if not re.search(r"[A-Z]", password):
        errors.append("Missing an uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("Missing a lowercase letter")
    if not re.search(r"[ @!#$%^&*()<>?/\\|}{~:]", password):
        errors.append("Missing a special character")

    return errors

def launch_password_checker():
    window = tk.Toplevel()
    window.title("🔑 Password Strength Checker")
    window.geometry("400x300")
    window.config(bg="#2c2c2c")

    label = tk.Label(window, text="Enter Password:", bg="#2c2c2c", fg="white")
    label.pack(pady=10)

    entry = tk.Entry(window, show="*", width=30)
    entry.pack(pady=5)

    result = tk.Label(window, text="", bg="#2c2c2c", fg="white", wraplength=300)
    result.pack(pady=15)

    def evaluate():
        pwd = entry.get()
        issues = check_strength(pwd)
        if issues:
            result.config(fg="red", text="❌ Weak password:\n- " + "\n- ".join(issues))
        else:
            result.config(fg="lightgreen", text="✅ Strong password!")

    tk.Button(window, text="Check", command=evaluate, bg="#444", fg="white").pack(pady=10)
