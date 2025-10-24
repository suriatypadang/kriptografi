import re
import math

def judul():
    print("=" * 60)
    print(" " * 15 + "PROGRAM KALKULATOR HYBRID")
    print("=" * 60)

# Pola valid untuk ekspresi matematika (hanya angka, spasi, dan operator dasar)
pola = r'^[0-9+\-*/().\s]+$'

def validasi_input(ekspresi):
    return bool(re.match(pola, ekspresi))

def proses_ekspresi(ekspresi):
    try:
        hasil = eval(ekspresi)
        return hasil
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def main():
    judul()
    ekspresi = input("Masukkan ekspresi matematika: ")

    print("\n>>> HASIL DIPROSES <<<")
    if not validasi_input(ekspresi):
        print("Input tidak valid! Gunakan hanya angka dan operator (+, -, *, /)")
        return

    hasil = proses_ekspresi(ekspresi)
    print(f"Ekspresi : {ekspresi}")
    print(f"Hasil    : {hasil}")

if __name__ == "__main__":
    main()
