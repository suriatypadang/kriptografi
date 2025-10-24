
def konversi_biner():
    print("\n KONVERSI DARI BINER ")
    biner = input("Masukkan bilangan biner (misal 1011): ")

    # Validasi agar hanya 0 dan 1
    if not all(ch in '01' for ch in biner):
        print(" Input tidak valid! Biner hanya boleh berisi 0 dan 1.")
        return

    desimal = int(biner, 2)
    heksa = hex(desimal).replace("0x", "").upper()

    print("\n=== HASIL KONVERSI ===")
    print(f" Biner        : {biner}")
    print(f" Desimal      : {desimal}")
    print(f" Heksadesimal : {heksa}")


def konversi_oktal():
    print("\n KONVERSI DARI OKTAL ")
    oktal = input("Masukkan bilangan oktal (misal 157): ")

    # Validasi agar hanya 0–7
    if not all(ch in '01234567' for ch in oktal):
        print(" Input tidak valid! Oktal hanya boleh berisi angka 0–7.")
        return

    desimal = int(oktal, 8)
    biner = bin(desimal).replace("0b", "")
    heksa = hex(desimal).replace("0x", "").upper()

    print("\n HASIL KONVERSI ")
    print(f" Oktal        : {oktal}")
    print(f" Desimal      : {desimal}")
    print(f" Biner        : {biner}")
    print(f" Heksadesimal : {heksa}")


def menu():
    while True:
        print("   PROGRAM KONVERSI BILANGAN")
        print("1. Konversi Biner ke Desimal & Heksadesimal")
        print("2. Konversi Oktal ke Desimal, Biner & Heksadesimal")
        print("3. Keluar")


        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            konversi_biner()
        elif pilihan == '2':
            konversi_oktal()
        elif pilihan == '3':
            print("Terima kasih! Program selesai ")
            break
        else:
            print(" Pilihan tidak valid! Coba lagi.")


# Jalankan program utama
if __name__ == "__main__":
    menu()
