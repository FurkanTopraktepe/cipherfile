import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import base64
import hashlib
import os

# Paroladan key üretme
def generate_key(password):
    hash = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash)

def encrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return
    
    key = generate_key(password)
    f = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            data = file.read()

        encrypted_data = f.encrypt(data)

        with open(file_path + ".enc", "wb") as file:
            file.write(encrypted_data)

        messagebox.showinfo("Success", "File encrypted successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return
    
    key = generate_key(password)
    f = Fernet(key)

    try:
        with open(file_path, "rb") as file:
            data = file.read()

        decrypted_data = f.decrypt(data)

        output_path = file_path.replace(".enc", "")
        with open(output_path, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", "File decrypted successfully!")

    except Exception:
        messagebox.showerror("Error", "Wrong password or invalid file!")

# GUI
root = tk.Tk()
root.title("CipherFile")
root.geometry("400x250")

tk.Label(root, text="CipherFile - File Encryption", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Enter Password:").pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Encrypt File", command=encrypt_file, width=20).pack(pady=10)
tk.Button(root, text="Decrypt File", command=decrypt_file, width=20).pack(pady=5)

root.mainloop()