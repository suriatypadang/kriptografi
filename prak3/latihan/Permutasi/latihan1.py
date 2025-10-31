import itertools

def semua_permutasi():
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    print("1. Permutasi Menyeluruh:", list(itertools.permutations(data)))
    k = int(input("Masukkan nilai k untuk permutasi sebagian: "))
    print("2. Permutasi Sebagian:", list(itertools.permutations(data, k)))

    print("3. Permutasi Keliling:")
    pertama = data[0]
    keliling = [[pertama] + list(p) for p in itertools.permutations(data[1:])]
    print(keliling)

    print("4. Permutasi Berkelompok:")
    grup = [data[:len(data)//2], data[len(data)//2:]]
    hasil = []
    for g in grup:
        for p in itertools.permutations(g):
            hasil.append(list(p))
    print(hasil)

semua_permutasi()
