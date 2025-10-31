# ==========================================
# Program Konversi Bilangan Heksadesimal ke Desimal, Biner, dan Oktal
# ==========================================

def heksa_ke_semua():
    print("=== KONVERSI BILANGAN HEKSADESIMAL ===")
    heksa = input("Masukkan bilangan heksadesimal (contoh: 1A, FF, 2B): ").strip()

    try:
        # Konversi heksadesimal ke desimal
        desimal = int(heksa, 16)
        # Konversi ke biner dan oktal
        biner = bin(desimal)[2:]
        oktal = oct(desimal)[2:]

        print("\n=== HASIL KONVERSI ===")
        print(f"Bilangan Heksadesimal : {heksa.upper()}")
        print(f"Bilangan Desimal      : {desimal}")
        print(f"Bilangan Biner        : {biner}")
        print(f"Bilangan Oktal        : {oktal}")

    except ValueError:
        print("⚠️ Error: Bilangan heksadesimal hanya boleh berisi angka 0–9 dan huruf A–F!")

# Jalankan program
heksa_ke_semua()
