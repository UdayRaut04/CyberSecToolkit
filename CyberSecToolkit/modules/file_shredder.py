import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox

def shred_file(path, passes=3):
    if not os.path.isfile(path):
        raise FileNotFoundError("File not found.")

    length = os.path.getsize(path)

    with open(path, "ba+", buffering=0) as f:
        for i in range(passes):
            f.seek(0)
            f.write(os.urandom(length))  # overwrite with random bytes
            f.flush()
            os.fsync(f.fileno())

    os.remove(path)

def launch_file_shredder():
    win = tk.Toplevel()
    win.title("🗑️ Secure File Shredder")
    win.geometry("400x200")
    win.config(bg="#1f1f1f")

    def browse_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                shred_file(file_path)
                messagebox.showinfo("Success", f"{os.path.basename(file_path)} securely shredded.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    tk.Label(win, text="Secure File Shredder", fg="white", bg="#1f1f1f", font=("Arial", 14)).pack(pady=20)
    tk.Button(win, text="🗂️ Select File to Shred", command=browse_file, bg="#d63031", fg="white", padx=10, pady=5).pack(pady=10)
