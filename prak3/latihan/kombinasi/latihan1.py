import itertools 

def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

def kombinasi(n, r):
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

def kombinasi_dengan_inisial():
    print("=== PROGRAM KOMBINASI DENGAN INISIAL HURUF ===")
    huruf = input("Masukkan kumpulan huruf (pisahkan dengan spasi): ").split()
    r = int(input("Masukkan jumlah huruf yang dipilih (r): "))
    n = len(huruf)
    print(f"\nJumlah kombinasi C({n},{r}) = {kombinasi(n, r)}")
    print("\n=== DAFTAR SEMUA KOMBINASI ===")
    for c in itertools.combinations(huruf, r):
        print(" ".join(c))
        
kombinasi_dengan_inisial()
