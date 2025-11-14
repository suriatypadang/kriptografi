import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# ---------- TABEL-TABEL DES (standar) ----------
PC_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC_2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

S_BOX = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

LEFT_SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# ---------- UTILITIES ----------
def permute(bit_list, table):
    return [bit_list[i-1] for i in table]

def xor_bits(a, b):
    return [x ^ y for x, y in zip(a, b)]

def chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def chunk_str(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

def bits_to_hex(bstr):
    # bstr: string of '0'/'1', pad left to full bytes
    if len(bstr) == 0:
        return ''
    # pad left so total bits a multiple of 4 for hex conversion
    pad = (4 - (len(bstr) % 4)) % 4
    bstr_p = ('0' * pad) + bstr
    n = int(bstr_p, 2)
    hx = hex(n)[2:].upper()
    # ensure full bytes shown
    byte_len = (len(bstr_p) + 7) // 8
    hx = hx.rjust(byte_len * 2, '0')
    return hx

# ---------- KEY SCHEDULE ----------
def generate_subkeys_from_key64(key64_str):
    # key64_str: 64-char string of '0'/'1'
    key_bits = [int(x) for x in key64_str]
    permuted = permute(key_bits, PC_1)  # 56 bits
    C = permuted[:28]
    D = permuted[28:]
    subkeys = []
    # store initial C0 D0 then after each shift
    C_values = [C[:]]
    D_values = [D[:]]
    for shift in LEFT_SHIFTS:
        C = C[shift:] + C[:shift]
        D = D[shift:] + D[:shift]
        C_values.append(C[:])
        D_values.append(D[:])
        CD = C + D
        Ki = permute(CD, PC_2)  # 48 bits
        subkeys.append(Ki)
    return subkeys, C_values, D_values

# ---------- FEISTEL FUNCTION (F) ----------
def sbox_substitution(bits48):
    blocks6 = chunk(bits48, 6)
    output_bits = []
    for i, b6 in enumerate(blocks6):
        row = (b6[0] << 1) | b6[5]
        col = (b6[1] << 3) | (b6[2] << 2) | (b6[3] << 1) | b6[4]
        val = S_BOX[i][row][col]
        out = [(val >> 3) & 1, (val >> 2) & 1, (val >> 1) & 1, val & 1]
        output_bits.extend(out)
    return output_bits

def feistel(R, K):
    # R: list of 32 bits, K: list of 48 bits
    R_exp = permute(R, E)  # 48 bits
    xr = xor_bits(R_exp, K)
    s_out = sbox_substitution(xr)
    p_out = permute(s_out, P)
    return p_out

# ---------- DES SINGLE-BLOCK ENCRYPT ----------
def des_block_encrypt(block64_bits, subkeys):
    block_ip = permute(block64_bits, IP)
    L = block_ip[:32]
    R = block_ip[32:]
    for i in range(16):
        F_out = feistel(R, subkeys[i])
        newR = xor_bits(L, F_out)
        L, R = R, newR
    preoutput = R + L  # swap
    cipher_bits = permute(preoutput, FP)
    return cipher_bits

# ---------- PADDING & BLOCKING ----------
def pkcs7_pad(data_bytes, block_size=8):
    pad_len = block_size - (len(data_bytes) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data_bytes + bytes([pad_len]) * pad_len

def split_blocks_padded(data_bytes, block_size=8):
    padded = pkcs7_pad(data_bytes, block_size)
    return [padded[i:i+block_size] for i in range(0, len(padded), block_size)]

# ---------- HIGH-LEVEL DES (ECB single-block for now) ----------
def encrypt_des_ecb(plaintext: str, key: str):
    # Key handling: limit to 8 chars, pad with null bytes
    if len(key) > 8:
        key = key[:8]
    key_bytes = key.encode('utf-8')
    if len(key_bytes) < 8:
        key_bytes = key_bytes + b'\x00' * (8 - len(key_bytes))
    key64 = ''.join(format(b, '08b') for b in key_bytes)[:64]

    subkeys, C_vals, D_vals = generate_subkeys_from_key64(key64)

    plain_bytes = plaintext.encode('utf-8')
    blocks = split_blocks_padded(plain_bytes, 8)

    cipher_bits_total = []
    per_block_cipher_bits = []
    for blk in blocks:
        blk_bits = []
        for b in blk:
            blk_bits.extend([int(x) for x in format(b, '08b')])
        blk_bits = blk_bits[:64]
        cipher_bits = des_block_encrypt(blk_bits, subkeys)
        per_block_cipher_bits.append(''.join(str(b) for b in cipher_bits))
        cipher_bits_total.extend(cipher_bits)

    cipher_bin_str = ''.join(str(b) for b in cipher_bits_total)
    cipher_hex = bits_to_hex(cipher_bin_str)
    return {
        'cipher_bin_str': cipher_bin_str,
        'cipher_hex': cipher_hex,
        'per_block_cipher_bits': per_block_cipher_bits,
        'subkeys': subkeys,
        'C_vals': C_vals,
        'D_vals': D_vals,
        'key64': key64,
        'blocks': blocks
    }

# ---------- GUI ----------
class DESGuiApp:
    def __init__(self, root):
        self.root = root
        root.title("DES Encryptor - GUI (perbaikan)")
        root.geometry("1100x720")

        frm_inputs = ttk.Frame(root, padding=8)
        frm_inputs.pack(fill='x')

        ttk.Label(frm_inputs, text="Plaintext:").grid(row=0, column=0, sticky='w')
        self.txt_plain = tk.Entry(frm_inputs, width=80)
        self.txt_plain.grid(row=0, column=1, sticky='w', padx=6, pady=4)

        ttk.Label(frm_inputs, text="Key (max 8 chars):").grid(row=1, column=0, sticky='w')
        self.txt_key = tk.Entry(frm_inputs, width=20)
        self.txt_key.grid(row=1, column=1, sticky='w', padx=6, pady=4)

        btn_encrypt = ttk.Button(frm_inputs, text="Encrypt", command=self.on_encrypt)
        btn_encrypt.grid(row=0, column=2, rowspan=2, padx=8)

        paned = ttk.PanedWindow(root, orient='horizontal')
        paned.pack(fill='both', expand=True, padx=6, pady=6)

        left = ttk.Frame(paned, width=540)
        right = ttk.Frame(paned, width=540)
        paned.add(left, weight=1)
        paned.add(right, weight=1)

        ttk.Label(left, text="Binary / Key / C0-D0 / C_i & D_i").pack(anchor='w')
        self.txt_left = scrolledtext.ScrolledText(left, wrap='none', width=70, height=40)
        self.txt_left.pack(fill='both', expand=True)

        ttk.Label(right, text="Subkeys (K1..K16) & Ciphertext").pack(anchor='w')
        self.txt_right = scrolledtext.ScrolledText(right, wrap='none', width=70, height=40)
        self.txt_right.pack(fill='both', expand=True)

    def on_encrypt(self):
        plain = self.txt_plain.get()
        key = self.txt_key.get()
        if key == "":
            messagebox.showwarning("Key missing", "Masukkan key (max 8 karakter).")
            return

        result = encrypt_des_ecb(plain, key)

        left_lines = []
        left_lines.append("Plaintext (raw):")
        left_lines.append(plain)
        left_lines.append("\nPlaintext blocks (after PKCS#7 padding) - bytes and binary:")
        for i, blk in enumerate(result['blocks']):
            bstr = ' '.join(f"{b:02X}" for b in blk)
            bbin = ''.join(format(b, '08b') for b in blk)
            left_lines.append(f"Block {i+1}: bytes: {bstr}    binary: {bbin}")

        left_lines.append("\nKey (padded 8 bytes) binary 64-bit:")
        left_lines.append(result['key64'])

        # PC-1 -> C0 & D0
        key_bits = [int(x) for x in result['key64']]
        permuted = permute(key_bits, PC_1)
        left_lines.append("\nPermutasi PC-1 (56 bit):")
        left_lines.append(''.join(str(x) for x in permuted))
        C0 = permuted[:28]
        D0 = permuted[28:]
        left_lines.append("\nC0 (28 bit): " + ''.join(str(x) for x in C0))
        left_lines.append("D0 (28 bit): " + ''.join(str(x) for x in D0))

        left_lines.append("\nC and D values:")
        # C_vals and D_vals include C0..C16 (length 17)
        for i in range(len(result['C_vals'])):
            Ci = ''.join(str(x) for x in result['C_vals'][i])
            Di = ''.join(str(x) for x in result['D_vals'][i])
            left_lines.append(f"C{i}: {Ci}")
            left_lines.append(f"D{i}: {Di}")

        # Right: subkeys + ciphertext
        right_lines = []
        right_lines.append("SUBKEYS (K1 .. K16) (each 48-bit):\n")
        for i, k in enumerate(result['subkeys']):
            kb = ''.join(str(x) for x in k)
            grouped = ' '.join(chunk_str(kb, 6))
            # hex representation of subkey (48 bits)
            khex = bits_to_hex(kb)
            right_lines.append(f"K{i+1}: {kb}   grouped6: {grouped}   hex: {khex}")

        right_lines.append("\nCIPHERTEXT PER BLOCK (binary):")
        for i, b in enumerate(result['per_block_cipher_bits']):
            right_lines.append(f"Block {i+1}: {b}")

        right_lines.append("\nCIPHERTEXT (concat binary):")
        right_lines.append(result['cipher_bin_str'])
        right_lines.append("\nCIPHERTEXT (HEX):")
        right_lines.append(result['cipher_hex'])

        # insert into widgets
        self.txt_left.delete('1.0', tk.END)
        self.txt_left.insert(tk.END, '\n'.join(left_lines))
        self.txt_right.delete('1.0', tk.END)
        self.txt_right.insert(tk.END, '\n'.join(right_lines))

        messagebox.showinfo("Selesai", "Enkripsi selesai. Lihat hasil di panel kanan.")

# ---------- MAIN ----------
def main():
    root = tk.Tk()
    app = DESGuiApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
