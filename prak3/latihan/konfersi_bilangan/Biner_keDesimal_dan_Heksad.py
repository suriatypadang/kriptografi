# ==========================================
# Program Konversi Bilangan Biner ke Desimal dan Heksadesimal
# ==========================================

def biner_ke_desimal_heksa():
    print("=== KONVERSI BILANGAN BINER ===")
    biner = input("Masukkan bilangan biner (contoh: 1010): ")

    try:
        # Konversi biner ke desimal
        desimal = int(biner, 2)
        # Konversi ke heksadesimal
        heksa = hex(desimal)[2:].upper()

        print("\n=== HASIL KONVERSI ===")
        print(f"Bilangan Biner       : {biner}")
        print(f"Bilangan Desimal     : {desimal}")
        print(f"Bilangan Heksadesimal: {heksa}")

    except ValueError:
        # Jika input bukan biner yang valid (hanya 0 dan 1)
        print("⚠️ Error: Masukkan hanya angka 0 dan 1 untuk bilangan biner!")

# Jalankan program
biner_ke_desimal_heksa()

