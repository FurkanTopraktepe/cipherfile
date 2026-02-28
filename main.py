import customtkinter as ctk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import base64
import hashlib
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

selected_file = None


# ================= ŞİFRELEME =================

def generate_key(password):
    hash = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash)


def xor_encrypt_decrypt(data, password):
    key = password.encode()
    output = bytearray()

    for i in range(len(data)):
        output.append(data[i] ^ key[i % len(key)])

    return bytes(output)


# ================= DOSYA SEÇ =================

def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename()
    if selected_file:
        file_label.configure(text=f"Seçildi: {os.path.basename(selected_file)}")


# ================= ŞİFRELE =================

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
        password_entry.delete(0, "end")

    except Exception as e:
        messagebox.showerror("Hata", str(e))


# ================= ÇÖZ =================

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
        password_entry.delete(0, "end")

    except Exception:
        messagebox.showerror("Hata", "Yanlış şifre veya geçersiz dosya!")


# ================= GUI =================

root = ctk.CTk()
root.title("Dosya Şifreleme Uygulaması")
root.geometry("500x540")
root.resizable(False, False)

title = ctk.CTkLabel(
    root,
    text="Dosya Şifreleme Uygulaması",
    font=ctk.CTkFont(size=22, weight="bold")
)
title.pack(pady=20)

select_button = ctk.CTkButton(
    root,
    text="Dosya Seç",
    command=select_file,
    width=200
)
select_button.pack(pady=10)

file_label = ctk.CTkLabel(
    root,
    text="Dosya seçilmedi"
)
file_label.pack(pady=5)

algorithm_label = ctk.CTkLabel(
    root,
    text="Algoritma Seç"
)
algorithm_label.pack(pady=10)

algorithm_var = ctk.StringVar(value="AES (Güçlü)")

algorithm_menu = ctk.CTkOptionMenu(
    root,
    values=["AES (Güçlü)", "XOR (Basit)"],
    variable=algorithm_var,
    width=200
)
algorithm_menu.pack(pady=5)

password_label = ctk.CTkLabel(
    root,
    text="Şifre Giriniz:"
)
password_label.pack(pady=10)

password_entry = ctk.CTkEntry(
    root,
    placeholder_text="Şifre",
    show="*",
    width=250
)
password_entry.pack(pady=5)

encrypt_button = ctk.CTkButton(
    root,
    text="Şifrele",
    command=encrypt_file,
    width=200
)
encrypt_button.pack(pady=15)

decrypt_button = ctk.CTkButton(
    root,
    text="Çöz",
    command=decrypt_file,
    width=200,
    fg_color="#C850C0",
    hover_color="#A832A8"
)
decrypt_button.pack(pady=5)

root.mainloop()
