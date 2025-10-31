import itertools

def permutasi_sebagian(arr, k):
    return list(itertools.permutations(arr, k))

data = [1, 2, 3, 4]
print(permutasi_sebagian(data, 2))

