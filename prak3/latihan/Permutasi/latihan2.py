import itertools

def atur_buku():
    n = int(input("Masukkan jumlah buku (n): "))
    r = int(input("Masukkan jumlah rak (r): "))
    buku = [f"Buku{i+1}" for i in range(n)]
    rak = [f"Rak{j+1}" for j in range(r)]
    semua_cara = list(itertools.product(buku, rak))
    print(f"Ada {len(semua_cara)} cara mengatur {n} buku di {r} rak:")
    for pasangan in semua_cara:
        print(pasangan)

atur_buku()
