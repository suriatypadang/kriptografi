import tkinter as tk
from tkinter import messagebox
import math
import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


root = tk.Tk()
root.title("RSA Dynamic – Enkripsi Banyak Huruf (Plaintext Bebas)")
root.geometry("700x650")

tk.Label(root, text="RSA – Input p & q, e otomatis acak", font=("Arial", 16)).pack(pady=5)

# Input p dan q
frame_pq = tk.Frame(root)
frame_pq.pack(pady=5)

tk.Label(frame_pq, text="Masukkan p (prima): ", font=("Arial", 12)).grid(row=0, column=0)
inp_p = tk.Entry(frame_pq, font=("Arial", 12), width=10)
inp_p.grid(row=0, column=1)

tk.Label(frame_pq, text="Masukkan q (prima): ", font=("Arial", 12)).grid(row=0, column=2)
inp_q = tk.Entry(frame_pq, font=("Arial", 12), width=10)
inp_q.grid(row=0, column=3)

# Input plaintext
tk.Label(root, text="Masukkan plaintext (huruf bebas, boleh ada spasi):", font=("Arial", 12)).pack()
inp = tk.Entry(root, font=("Arial", 14), width=40)
inp.pack(pady=5)

# Output box
output = tk.Text(root, width=90, height=25, font=("Consolas", 10))
output.pack(pady=10)

def tampil(txt):
    output.delete(1.0, tk.END)
    output.insert(tk.END, txt)

# -------------------------
# Proses RSA
# -------------------------
def proses_rsa():
    text = inp.get()
    p_val = inp_p.get()
    q_val = inp_q.get()

    # --- VALIDASI: plaintext bebas ---
    if len(text.strip()) == 0:
        messagebox.showerror("Error", "Plaintext tidak boleh kosong!")
        return

    if not text.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Plaintext hanya boleh huruf A-Z dan spasi!")
        return

    # Validasi p & q
    try:
        p = int(p_val)
        q = int(q_val)
    except:
        messagebox.showerror("Error", "p dan q harus angka!")
        return

    if not (is_prime(p) and is_prime(q)):
        messagebox.showerror("Error", "p dan q harus bilangan prima!")
        return

    # Hitung RSA
    n = p * q
    phi = (p - 1) * (q - 1)

    # Cari e otomatis (acak)
    candidates = [i for i in range(50, 200) if gcd(i, phi) == 1]

    if not candidates:
        messagebox.showerror("Error", "Tidak ada nilai e yang cocok!")
        return

    e = random.choice(candidates)
    d = mod_inverse(e, phi)

    # Tabel enkripsi
    tabel = "HURUF  | ASCII | ENKRIPSI (cipher)\n"
    tabel += "-" * 40 + "\n"

    decrypted_result = ""

    for ch in text:
        ascii_val = 32 if ch == " " else ord(ch)
        cipher = pow(ascii_val, e, n)
        dec = pow(cipher, d, n)

        decrypted_result += " " if dec == 32 else chr(dec)

        tabel += f"{ch:6} | {ascii_val:5} | {cipher:5}\n"

    hasil = f"""
=== RSA Enkripsi Dinamis ===

p = {p}
q = {q}
n = {n}
phi(n) = {phi}

e (otomatis) = {e}
d = {d}

Plaintext:
{text}

Tabel Enkripsi:
{tabel}

Hasil Dekripsi:
{decrypted_result}
"""

    tampil(hasil)

# Tombol proses
tk.Button(root, text="Proses RSA", font=("Arial", 12), width=20, command=proses_rsa).pack()

root.mainloop()
