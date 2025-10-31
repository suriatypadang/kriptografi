# ==========================================
# Program Konversi Bilangan Oktal ke Desimal, Biner, dan Heksadesimal
# ==========================================

def oktal_ke_semua():
    print("=== KONVERSI BILANGAN OKTAL ===")
    oktal = input("Masukkan bilangan oktal (contoh: 17): ")

    try:
        # Konversi ke desimal
        desimal = int(oktal, 8)
        # Konversi ke biner dan heksadesimal
        biner = bin(desimal)[2:]
        heksa = hex(desimal)[2:].upper()

        print("\n=== HASIL KONVERSI ===")
        print(f"Bilangan Oktal       : {oktal}")
        print(f"Bilangan Desimal     : {desimal}")
        print(f"Bilangan Biner       : {biner}")
        print(f"Bilangan Heksadesimal: {heksa}")

    except ValueError:
        print("⚠️ Error: Bilangan oktal hanya boleh berisi angka 0–7!")

# Jalankan program
oktal_ke_semua()
