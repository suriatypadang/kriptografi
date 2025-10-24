def konversi_biner():
    print("\n KONVERSI DARI BINER ")
    biner = input("Masukkan bilangan biner (misal 1011): ")

    # Validasi agar hanya 0 dan 1
    if not all(ch in '01' for ch in biner):
        print(" Input tidak valid! Bilangan biner hanya boleh berisi 0 dan 1.")
        return

    # Konversi ke Desimal
    desimal = int(biner, 2)

    # Konversi ke Heksadesimal (tanpa prefix '0x')
    heksa = hex(desimal).replace("0x", "").upper()

    # Tampilkan hasil
    print("\n=== HASIL KONVERSI ===")
    print(f" Biner        : {biner}")
    print(f" Desimal      : {desimal}")
    print(f" Heksadesimal : {heksa}")


def menu():
    while True:
        print("   PROGRAM KONVERSI BILANGAN")
        print("1. Konversi Biner ke Desimal dan Heksadesimal")
        print("2. Keluar")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == '1':
            konversi_biner()
        elif pilihan == '2':
            print("Terima kasih! Program selesai ")
            break
        else:
            print(" Pilihan tidak valid! Coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    menu()
