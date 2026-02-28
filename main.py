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

def xor_encrypt_decrypt(data, password):
    key = password.encode()
    output = bytearray()

    for i in range(len(data)):
        output.append(data[i] ^ key[i % len(key)])

    return bytes(output)

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    if selected_file:
        file_label.config(text=f"Seçildi: {os.path.basename(selected_file)}")

def encrypt_file():
    global selected_file
    if not selected_file:
        messagebox.showerror("Hata", "Önce bir dosya seçmelisiniz.")
        return

    password = password_entry.get()
    if not password:
        messagebox.showerror("Hata", "Lütfen bir şifre giriniz.")
        return

    try:
        algorithm = algorithm_var.get()

        with open(selected_file, "rb") as file:
            data = file.read()

        if algorithm == "AES (Güçlü)":
            key = generate_key(password)
            f = Fernet(key)
            encrypted_data = f.encrypt(data)

        elif algorithm == "XOR (Basit)":
            encrypted_data = xor_encrypt_decrypt(data, password)

        output_path = selected_file + ".enc"

        with open(output_path, "wb") as file:
            file.write(encrypted_data)

        messagebox.showinfo("Başarılı", "Dosya başarıyla şifrelendi!")
        password_entry.delete(0, tk.END)

    except Exception as e:
            messagebox.showerror("Hata", str(e))

def decrypt_file():
    global selected_file
    if not selected_file:
        messagebox.showerror("Hata", "Önce bir dosya seçmelisiniz.")
        return

    password = password_entry.get()
    if not password:
        messagebox.showerror("Hata", "Lütfen bir şifre giriniz.")
        return

    try:
        algorithm = algorithm_var.get()

        with open(selected_file, "rb") as file:
            data = file.read()

        if algorithm == "AES (Güçlü)":
            key = generate_key(password)
            f = Fernet(key)
            decrypted_data = f.decrypt(data)

        elif algorithm == "XOR (Basit)":
            decrypted_data = xor_encrypt_decrypt(data, password)

        if selected_file.endswith(".enc"):
            output_path = selected_file[:-4]
        else:
            output_path = selected_file + "_decrypted"

        with open(output_path, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo("Başarılı", "Dosya başarıyla çözüldü!")
        password_entry.delete(0, tk.END)

    except Exception:
        messagebox.showerror("Hata", "Yanlış şifre veya geçersiz dosya!")

# GUI
root = tk.Tk()  
root.title("Dosya Şifreleme Uygulaması")
root.geometry("450x350")
root.resizable(False, False)
root.configure(bg="#2B2D42") 

title = tk.Label(root, text="Dosya Şifreleme Uygulaması", font=("Arial", 18, "bold"), bg="#2B2D42", fg="#FF79C6")
title.pack(pady=10)

tk.Button(root, text="Dosya Seç", command=select_file, width=20, bg="#8D99AE", fg="black", activebackground="#8D99AE").pack(pady=5)

file_label = tk.Label(root, text="Dosya seçilmedi", fg="white", bg="#2B2D42")
file_label.pack(pady=5)

# Algoritma seçimi
tk.Label(root, text="Algoritma Seç", bg="#2B2D42", fg="white").pack(pady=5)

algorithm_var = tk.StringVar(value="AES (Güçlü)")

algorithm_menu = tk.OptionMenu(root, algorithm_var, "AES (Güçlü)", "XOR (Basit)")
algorithm_menu.config(bg="#8D99AE", fg="black", width=15, relief="flat")
algorithm_menu.pack(pady=5)

tk.Label(root, text="Şifre Giriniz:", bg="#2B2D42", fg="white").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Şifrele", command=encrypt_file, width=20, bg="#9B5DE5", fg="white", activebackground="#B48CD4").pack(pady=10)
tk.Button(root, text="Çöz", command=decrypt_file, width=20,bg="#F15BB5", fg="white", activebackground="#E09BD3").pack(pady=5)

root.mainloop()

