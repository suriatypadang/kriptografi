import itertools

def permutasi_keliling(arr):
    if len(arr) == 1:
        return [arr]
    pertama = arr[0]
    permutasi_penuh = list(itertools.permutations(arr[1:]))
    return [[pertama] + list(perm) for perm in permutasi_penuh]

data = [1, 2, 3]
print(permutasi_keliling(data))
