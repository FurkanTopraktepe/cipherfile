# 🔐 CipherFile – Python Dosya Şifreleme Uygulaması

## 📌 Proje Amacı

CipherFile, kullanıcıların dosyalarını parola ile şifreleyip tekrar çözebilmesini sağlayan basit bir masaüstü uygulamasıdır.
Proje, simetrik şifreleme mantığını ve GUI geliştirmeyi öğrenmek amacıyla geliştirilmiştir.

---

## ⚙️ Kullanılan Teknolojiler

* Python 3.x
* Tkinter (Grafik Arayüz)
* cryptography kütüphanesi
* Fernet (AES tabanlı simetrik şifreleme)

---

## 🔐 Şifreleme Mantığı

* Kullanıcı bir parola girer.
* Paroladan SHA-256 algoritması ile bir anahtar türetilir.
* Bu anahtar, Fernet sistemi ile dosyayı şifrelemek veya çözmek için kullanılır.
* Şifrelenmiş dosyalar `.enc` uzantısı ile kaydedilir.
* Yanlış parola girildiğinde hata mesajı gösterilir.

---

## 🖥️ Uygulama Özellikleri

* Dosya seçme
* Parola ile şifreleme
* Parola ile çözme
* Yanlış parola kontrolü
* Kullanıcı dostu arayüz

---

## 🚀 Kurulum

1. Python 3.x kurulu olmalıdır.
2. Proje klasörüne girin:

```bash
cd CipherFile
```

3. Sanal ortam oluşturun:

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

Windows için:

```bash
python -m venv venv
venv\Scripts\activate
```

4. Gerekli kütüphaneleri yükleyin:

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Çalıştırma

```bash
python main.py
```

---

## 📂 Proje Yapısı

```
CipherFile/
│
├── main.py
├── requirements.txt
└── README.md
```


---

## 🎓 Akademik Amaç

Bu proje ile:

* Simetrik şifreleme mantığını öğrendim.
* Parola tabanlı anahtar üretimi uyguladım.
* Python GUI geliştirme deneyimi kazandım.

---

# ✅ Not

Bu uygulama eğitim amaçlı geliştirilmiştir.

---
