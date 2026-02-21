import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import base64
import hashlib
import os

selected_file = None

def generate_key(password):
    hash = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash)

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    if selected_file:
        file_label.config(text=f"Selected: {os.path.basename(selected_file)}")

def encrypt_file():
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "Please select a file first.")
        return

    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    key = generate_key(password)
    f = Fernet(key)

    try:
        with open(selected_file, "rb") as file:
            data = file.read()

        encrypted_data = f.encrypt(data)

        output_path = selected_file + ".enc"
        with open(output_path, "wb") as file:
            file.write(encrypted_data)

        messagebox.showinfo("Success", "File encrypted successfully!")
        password_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_file():
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "Please select a file first.")
        return

    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    key = generate_key(password)
    f = Fernet(key)

    try:
        with open(selected_file, "rb") as file:
            data = file.read()

        decrypted_data = f.decrypt(data)

        if selected_file.endswith(".enc"):
            output_path = selected_file[:-4]
        else:
            output_path = selected_file + "_decrypted"

        with open(output_path, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", "File decrypted successfully!")
        password_entry.delete(0, tk.END)

    except Exception:
        messagebox.showerror("Error", "Wrong password or invalid file!")

# GUI
root = tk.Tk()
root.title("CipherFile")
root.geometry("450x300")
root.resizable(False, False)

title = tk.Label(root, text="CipherFile", font=("Arial", 18, "bold"))
title.pack(pady=10)

tk.Button(root, text="Select File", command=select_file, width=20).pack(pady=5)

file_label = tk.Label(root, text="No file selected", fg="gray")
file_label.pack(pady=5)

tk.Label(root, text="Enter Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Encrypt", command=encrypt_file, width=20).pack(pady=10)
tk.Button(root, text="Decrypt", command=decrypt_file, width=20).pack(pady=5)

root.mainloop()