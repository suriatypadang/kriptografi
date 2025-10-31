def konversi_bilangan():
    desimal = int(input("Masukkan bilangan desimal: "))
    biner = bin(desimal)[2:]
    oktal = oct(desimal)[2:]
    heksadesimal = hex(desimal)[2:]

    print(f"Bilangan desimal: {desimal}")
    print(f"Biner: {biner}")
    print(f"Oktal: {oktal}")
    print(f"Heksadesimal: {heksadesimal}")

konversi_bilangan()
