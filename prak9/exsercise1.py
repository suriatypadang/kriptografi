import tkinter as tk
from tkinter import messagebox

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


root = tk.Tk()
root.title("RSA Soal 1 – Enkripsi Banyak Huruf")
root.geometry("650x550")

tk.Label(root, text="RSA Soal 1 (p=17, q=11, e=7)", font=("Arial", 15)).pack(pady=5)
tk.Label(root, text="Masukkan plaintext minimal 8 huruf:", font=("Arial", 12)).pack()

inp = tk.Entry(root, font=("Arial", 14), width=40)
inp.pack(pady=5)

output = tk.Text(root, width=80, height=25, font=("Consolas", 10))
output.pack(pady=10)

def tampil(txt):
    output.delete(1.0, tk.END)
    output.insert(tk.END, txt)

def proses_rsa():
    text = inp.get()

    if len(text) < 8:
        messagebox.showerror("Error", "Minimal 8 huruf!")
        return

    if not text.replace(" ", "").isalpha():  # boleh ada spasi
        messagebox.showerror("Error", "Hanya huruf A-Z dan spasi!")
        return

    p = 17
    q = 11
    e = 7

    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)

    # Buat tabel
    tabel = "HURUF  | ASCII | ENKRIPSI (cipher)\n"
    tabel += "-" * 40 + "\n"

    decrypted_result = ""

    for ch in text:
        if ch == " ":
            ascii_val = 32
        else:
            ascii_val = ord(ch)

        cipher = pow(ascii_val, e, n)
        dec = pow(cipher, d, n)

        # Mengubah kembali ke huruf
        if dec == 32:
            decrypted_result += " "
        else:
            decrypted_result += chr(dec)

        tabel += f"{ch:6} | {ascii_val:5} | {cipher:5}\n"

    hasil = f"""
=== RSA Soal 1 (Tabel Enkripsi Banyak Huruf) ===

p = {p}
q = {q}
e = {e}
n = {n}
phi = {phi}
d = {d}

Plaintext:
{text}

Hasil Tabel Enkripsi:
{tabel}

Hasil Dekripsi:
{decrypted_result}
"""

    tampil(hasil)

tk.Button(root, text="Proses RSA", font=("Arial", 12), width=20, command=proses_rsa).pack()

root.mainloop()
