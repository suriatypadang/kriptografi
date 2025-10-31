def transposisi_cipher(plaintext):
    part_length = len(plaintext) // 4
    parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]

    print("Bagian plaintext:")
    for i, part in enumerate(parts):
        print(f"Bagian {i + 1}: '{part}'")

    ciphertext = ""
    for col in range(4):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
                print(f"Menambahkan '{part[col]}' dari Bagian {parts.index(part) + 1} ke ciphertext.")

    return ciphertext


plaintext = input("Masukkan plaintext: ")
ciphertext = transposisi_cipher(plaintext)
print(f"Ciphertext: '{ciphertext}'")
