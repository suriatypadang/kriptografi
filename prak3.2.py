def konversi_biner():
    print("\n KONVERSI DARI BINER ")
    biner = input("Masukkan bilangan biner (misal 1011): ")

    if not all(ch in '01' for ch in biner):
        return

    desimal = int(biner, 2)
    heksa = hex(desimal).replace("0x", "").upper()

    print("\n HASIL KONVERSI ")
    print(f" Biner        : {biner}")
    print(f" Desimal      : {desimal}")
    print(f" Heksadesimal : {heksa}")


def konversi_oktal():
    print("\n KONVERSI DARI OKTAL ")
    oktal = input("Masukkan bilangan oktal  ")

    

    desimal = int(oktal, 8)
    biner = bin(desimal).replace("0b", "")
    heksa = hex(desimal).replace("0x", "").upper()

    print("\n HASIL KONVERSI ")
    print(f" Oktal        : {oktal}")
    print(f" Desimal      : {desimal}")
    print(f" Biner        : {biner}")
    print(f" Heksadesimal : {heksa}")


def konversi_heksadesimal():
    print("\n KONVERSI DARI HEKSADESIMAL ")
    heksa = input("Masukkan bilangan heksadesimal").upper()
    
    if not all(ch in '0123456789ABCDEF' for ch in heksa):
        print(" Input tidak valid! Heksadesimal hanya boleh berisi 0–9 dan A–F.")
        return

    desimal = int(heksa, 16)
    biner = bin(desimal).replace("0b", "")
    oktal = oct(desimal).replace("0o", "")

    print("\n=== HASIL KONVERSI ===")
    print(f" Heksadesimal : {heksa}")
    print(f" Desimal      : {desimal}")
    print(f" Biner        : {biner}")
    print(f" Oktal        : {oktal}")


def menu():
    while True:
        print("   PROGRAM KONVERSI BILANGAN")
        print("1. Biner → Desimal & Heksadesimal")
        print("2. Oktal → Desimal, Biner & Heksadesimal")
        print("3. Heksadesimal → Desimal, Biner & Oktal")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            konversi_biner()
        elif pilihan == '2':
            konversi_oktal()
        elif pilihan == '3':
            konversi_heksadesimal()
        elif pilihan == '4':
            print("Terima kasih! Program selesai ")
            break
        else:
            print(" Pilihan tidak valid! Coba lagi.")


# Jalankan program utama
if __name__ == "__main__":
    menu()
