import tkinter as tk
from tkinter import ttk
import random

# ================== FUNGSI MATEMATIKA ==================
def modinv(a, p):
    for i in range(1, p):
        if (a * i) % p == 1:
            return i
    return None

def log(teks):
    txt_log.insert(tk.END, teks + "\n")
    txt_log.see(tk.END)

# ================== GLOBAL ==================
ciphertext = []

# ================== PEMBANGKITAN KUNCI ==================
def pembangkitan_kunci():
    txt_log.delete(1.0, tk.END)
    frame_table.pack_forget()

    p = int(ent_p.get())
    g = int(ent_g.get())
    x = int(ent_x.get())

    log("=== PROSES PEMBANGKITAN KUNCI ELGAMAL ===\n")

    log("Langkah 1:")
    log("Menentukan bilangan prima p")
    log("Syarat: p > 2 dan p bilangan prima")
    log(f"p = {p}\n")

    log("Langkah 2:")
    log("Memilih bilangan acak g dan x")
    log("Syarat:")
    log("1 < g < p")
    log("1 < x < p − 2")
    log(f"g = {g}")
    log(f"x = {x}\n")

    log("Langkah 3:")
    log("Menghitung nilai y")
    log("Rumus: y = g^x mod p")
    log(f"y = {g}^{x} mod {p}")

    y = pow(g, x, p)
    log(f"Hasil y = {y}\n")

    log("Hasil Pembangkitan Kunci:")
    log(f"Kunci Publik  : (y, g, p) = ({y}, {g}, {p})")
    log(f"Kunci Privat  : (x, p)    = ({x}, {p})")

    ent_y.delete(0, tk.END)
    ent_y.insert(0, str(y))

# ================== ENKRIPSI ==================
def enkripsi():
    txt_log.delete(1.0, tk.END)
    table.delete(*table.get_children())
    frame_table.pack(fill="both", padx=10, pady=10)

    p = int(ent_p.get())
    g = int(ent_g.get())
    y = int(ent_y.get())
    plaintext = ent_plain.get().upper()

    k = random.randint(2, p - 2)

    log("=== PROSES ENKRIPSI ELGAMAL ===")
    log(f"Plaintext = {plaintext}")
    log(f"Bilangan acak k = {k}\n")

    ciphertext.clear()

    for i, ch in enumerate(plaintext):
        m = ord(ch)
        a = pow(g, k, p)
        b = (m * pow(y, k, p)) % p

        ciphertext.append((a, b))

        table.insert("", "end", values=(
            i + 1,
            "Enkripsi",
            f"{ch} → {m}",
            f"a = {g}^{k} mod {p}\n"
            f"b = {m} × {y}^{k} mod {p}",
            f"({a}, {b})"
        ))

    ent_cipher.delete(0, tk.END)
    ent_cipher.insert(0, str(ciphertext))

# ================== DEKRIPSI (TANPA LOG) ==================
def dekripsi():
    txt_log.delete(1.0, tk.END)   # kosongkan log, tidak ditulis apa-apa
    table.delete(*table.get_children())
    frame_table.pack(fill="both", padx=10, pady=10)

    p = int(ent_p.get())
    x = int(ent_x.get())
    hasil = ""

    for i, (a, b) in enumerate(ciphertext):
        ax = pow(a, x, p)
        inv = modinv(ax, p)
        m = (b * inv) % p
        huruf = chr(m)
        hasil += huruf

        table.insert("", "end", values=(
            i + 1,
            "Dekripsi",
            f"(a,b)=({a},{b})",
            f"{b} × {inv} mod {p}",
            f"{m} → {huruf}"
        ))

    ent_hasil.delete(0, tk.END)
    ent_hasil.insert(0, hasil)

# ================== GUI ==================
root = tk.Tk()
root.title("ElGamal GUI ")
root.geometry("1100x750")

style = ttk.Style()
style.configure("Treeview", rowheight=45)

frame = ttk.LabelFrame(root, text="Input Data")
frame.pack(fill="x", padx=10, pady=10)

labels = [
    "p (bilangan prima)",
    "g (bilangan acak)",
    "x (kunci privat)",
    "y (kunci publik)",
    "Plaintext",
    "Ciphertext",
    "Hasil Plaintext"
]

entries = []
for i, lbl in enumerate(labels):
    ttk.Label(frame, text=lbl, width=20).grid(row=i, column=0, sticky="w", pady=3)
    e = ttk.Entry(frame, width=60)
    e.grid(row=i, column=1, pady=3)
    entries.append(e)

ent_p, ent_g, ent_x, ent_y, ent_plain, ent_cipher, ent_hasil = entries

ttk.Button(frame, text="Pembangkitan Kunci", command=pembangkitan_kunci).grid(row=0, column=2, padx=5)
ttk.Button(frame, text="Enkripsi", command=enkripsi).grid(row=1, column=2, padx=5)
ttk.Button(frame, text="Dekripsi", command=dekripsi).grid(row=2, column=2, padx=5)

# ================== TABEL ENKRIPSI & DEKRIPSI ==================
frame_table = ttk.LabelFrame(root, text="Tabel Proses Enkripsi & Dekripsi")

columns = ("No", "Proses", "Data", "Perhitungan", "Hasil")
table = ttk.Treeview(frame_table, columns=columns, show="headings")

table.column("No", width=50, anchor="center")
table.column("Proses", width=100, anchor="center")
table.column("Data", width=150, anchor="center")
table.column("Perhitungan", width=450, anchor="w")
table.column("Hasil", width=150, anchor="center")

for col in columns:
    table.heading(col, text=col)

scroll = ttk.Scrollbar(frame_table, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scroll.set)

table.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

# ================== LOG PEMBANGKITAN KUNCI ==================
txt_log = tk.Text(root, height=12, font=("Consolas", 10))
txt_log.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
