import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import base64
import os
import hashlib

def generate_key(password: str) -> bytes:
    """Generate a Fernet key from the given password"""
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt_file(file_path, password):
    key = generate_key(password)
    fernet = Fernet(key)
    
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)

    encrypted_path = file_path + ".enc"
    with open(encrypted_path, "wb") as f:
        f.write(encrypted)

    return encrypted_path

def decrypt_file(file_path, password):
    key = generate_key(password)
    fernet = Fernet(key)
    
    with open(file_path, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)

    if file_path.endswith(".enc"):
        decrypted_path = file_path[:-4] + "_decrypted"
    else:
        decrypted_path = file_path + "_decrypted"

    with open(decrypted_path, "wb") as f:
        f.write(decrypted)

    return decrypted_path

def launch_file_encryptor():
    win = tk.Toplevel()
    win.title("🔐 File Encryptor/Decryptor")
    win.geometry("400x300")
    win.config(bg="#2c2c2c")

    status_label = tk.Label(win, text="", bg="#2c2c2c", fg="white", wraplength=350)
    status_label.pack(pady=10)

    def select_file():
        file_path = filedialog.askopenfilename()
        return file_path

    def encrypt_ui():
        file_path = select_file()
        if not file_path:
            return
        pwd = password_entry.get()
        if not pwd:
            messagebox.showerror("Error", "Please enter a password.")
            return
        try:
            result = encrypt_file(file_path, pwd)
            status_label.config(fg="lightgreen", text=f"✅ Encrypted: {result}")
        except Exception as e:
            status_label.config(fg="red", text=f"❌ Error: {str(e)}")

    def decrypt_ui():
        file_path = select_file()
        if not file_path:
            return
        pwd = password_entry.get()
        if not pwd:
            messagebox.showerror("Error", "Please enter a password.")
            return
        try:
            result = decrypt_file(file_path, pwd)
            status_label.config(fg="lightgreen", text=f"✅ Decrypted: {result}")
        except Exception as e:
            status_label.config(fg="red", text=f"❌ Error: {str(e)}")

    tk.Label(win, text="Enter password:", bg="#2c2c2c", fg="white").pack(pady=5)
    password_entry = tk.Entry(win, show="*", width=30)
    password_entry.pack(pady=5)

    tk.Button(win, text="Encrypt File", command=encrypt_ui, bg="#444", fg="white").pack(pady=10)
    tk.Button(win, text="Decrypt File", command=decrypt_ui, bg="#444", fg="white").pack(pady=5)
