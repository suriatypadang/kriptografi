def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


# Input aturan substitusi dari user
aturan_substitusi = {}
jumlah_aturan = int(input("Masukkan jumlah aturan substitusi: "))

for i in range(jumlah_aturan):
    huruf_asli = input(f"Masukkan huruf asli ke-{i+1}: ").upper()
    huruf_ganti = input(f"Masukkan huruf pengganti untuk '{huruf_asli}': ").upper()
    aturan_substitusi[huruf_asli] = huruf_ganti

# Input plaintext dari user
plaintext = input("Masukkan plaintext: ").upper()

# Proses enkripsi
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# Hasil
print("\n=== HASIL ENKRIPSI ===")
print(f"Plaintext : {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Aturan substitusi yang digunakan: {aturan_substitusi}")
