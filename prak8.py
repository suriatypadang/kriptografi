import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox

# ----------------- AES tables (S-box / Rcon) -----------------
SBOX = [
0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,
0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,
0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,
0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,
0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,
0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,
0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,
0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,
0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,
0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,
0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,
0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,
0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,
0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,
0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
]

RCON = [0x00,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]

# ----------------- Helper functions -----------------
def to_hex(b): return f"{b:02X}"

def pad16(s): return (s[:16]).ljust(16, "\x00")

def text_to_bytes(s):
    s16 = pad16(s)
    return [ord(c) for c in s16]

def bytes_to_matrix_colmajor(bts):
    m = [[0]*4 for _ in range(4)]
    for c in range(4):
        for r in range(4):
            m[r][c] = bts[c*4 + r]
    return m

def matrix_to_hex(m):
    return "\n".join(" ".join(to_hex(m[r][c]) for c in range(4)) for r in range(4))

def words_from_key_bytes(key_bytes):
    return [[key_bytes[4*c + r] for r in range(4)] for c in range(4)]

def rot_word(w): return w[1:] + w[:1]

def sub_word(w): return [SBOX[b] for b in w]

def xor_words(a,b): return [a[i]^b[i] for i in range(4)]

def gmul(a,b):
    res=0
    for _ in range(8):
        if b&1: res^=a
        hi=a&0x80
        a=(a<<1)&0xFF
        if hi:a^=0x1B
        b>>=1
    return res

# ----------------- MixColumns (custom per your matrix) -----------------
def mix_single_column(col):
    a0, a1, a2, a3 = col
    return [
        gmul(a0, 2) ^ gmul(a1, 1) ^ gmul(a2, 1) ^ gmul(a3, 3),   # 02 01 01 03
        gmul(a0, 2) ^ gmul(a1, 1) ^ gmul(a2, 3) ^ gmul(a3, 1),   # 02 01 03 01
        gmul(a0, 3) ^ gmul(a1, 1) ^ gmul(a2, 2) ^ gmul(a3, 1),   # 03 01 02 01
        gmul(a0, 1) ^ gmul(a1, 3) ^ gmul(a2, 1) ^ gmul(a3, 2),   # 01 03 01 02
    ]

def mix_columns(state):
    out=[[0]*4 for _ in range(4)]
    for c in range(4):
        col=[state[r][c] for r in range(4)]
        res=mix_single_column(col)
        for r in range(4):
            out[r][c]=res[r]&0xFF
    return out

def sub_bytes_state(s):
    return [[SBOX[s[r][c]] for c in range(4)] for r in range(4)]

def shift_rows(s):
    out=[[0]*4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            out[r][c]=s[r][(c+r)%4]
    return out

def add_round_key(s,k):
    return [[(s[r][c]^k[r][c])&0xFF for c in range(4)] for r in range(4)]

# ----------------- Key Expansion Verbose -----------------
def key_expansion_verbose(keytext, log_fn):
    key_bytes=text_to_bytes(keytext)
    w=words_from_key_bytes(key_bytes)  # w0..w3
    log_fn("=== KEY EXPANSION (AES-128) ===")
    for i in range(4):
        log_fn(f"w{i}: " + " ".join(to_hex(x) for x in w[i]))
    log_fn("")

    for i in range(4,44):
        temp=w[i-1].copy()
        if i%4==0:
            log_fn(f"--- Generating w{i} (i={i}) ---")
            log_fn("Temp before RotWord: " + " ".join(to_hex(x) for x in temp))
            temp = rot_word(temp)
            log_fn("After RotWord      : " + " ".join(to_hex(x) for x in temp))
            temp = sub_word(temp)
            log_fn("After SubWord      : " + " ".join(to_hex(x) for x in temp))
            rcon_word = [RCON[i//4], 0x00, 0x00, 0x00]
            log_fn("Rcon               : " + " ".join(to_hex(x) for x in rcon_word))
            temp = xor_words(temp, rcon_word)
            log_fn("After XOR Rcon     : " + " ".join(to_hex(x) for x in temp))
        neww = xor_words(w[i-4], temp)
        w.append(neww)
        log_fn(f"w{i}: " + " ".join(to_hex(x) for x in neww))
    log_fn("")

    round_keys=[]
    for r in range(11):
        words=w[4*r:4*r+4]
        # convert words to 4x4 matrix (rows x cols)
        rk=[[words[c][r2] for c in range(4)] for r2 in range(4)]
        round_keys.append(rk)
        log_fn(f"RoundKey {r}:\n" + matrix_to_hex(rk) + "\n")
    return round_keys

# ----------------- AES Encryption Verbose (clean, step-by-step) -----------------
def aes_encrypt_block_verbose(pt_bytes, round_keys, log_fn):
    state = bytes_to_matrix_colmajor(pt_bytes)
    log_fn("=== INITIAL ROUND (AddRoundKey 0) ===")
    log_fn("State before AddRoundKey 0:")
    log_fn(matrix_to_hex(state))
    state = add_round_key(state, round_keys[0])
    log_fn("State after  AddRoundKey 0:")
    log_fn(matrix_to_hex(state))
    log_fn("")

    for r in range(1,10):
        log_fn(f"=== ROUND {r} ===")
        log_fn("[1] SubBytes")
        state = sub_bytes_state(state)
        log_fn(matrix_to_hex(state))
        log_fn("[2] ShiftRows")
        state = shift_rows(state)
        log_fn(matrix_to_hex(state))
        log_fn("[3] MixColumns")
        state = mix_columns(state)
        log_fn(matrix_to_hex(state))
        log_fn(f"[4] AddRoundKey (K{r})")
        state = add_round_key(state, round_keys[r])
        log_fn(matrix_to_hex(state))
        log_fn("")

    log_fn("=== FINAL ROUND (10) ===")
    log_fn("[1] SubBytes")
    state = sub_bytes_state(state)
    log_fn(matrix_to_hex(state))
    log_fn("[2] ShiftRows")
    state = shift_rows(state)
    log_fn(matrix_to_hex(state))
    log_fn("[3] AddRoundKey (K10)")
    state = add_round_key(state, round_keys[10])
    log_fn(matrix_to_hex(state))
    log_fn("")

    # produce ciphertext (column-major)
    cipher=[]
    for c in range(4):
        for r in range(4):
            cipher.append(state[r][c] & 0xFF)
    return cipher

# ----------------- Full AES Encryption (single block) -----------------
def aes_encrypt_full_verbose(pt_text, key_text, log_fn):
    pt_block = pad16(pt_text)
    pt_bytes = [ord(c) for c in pt_block]
    log_fn("=== INPUT CONVERSION ===")
    log_fn("Plaintext ASCII bytes: " + " ".join(str(ord(c)) for c in pt_block))
    log_fn("Plaintext HEX        : " + " ".join(to_hex(b) for b in pt_bytes))
    log_fn("")
    log_fn("CipherKey ASCII bytes: " + " ".join(str(ord(c)) for c in pad16(key_text)))
    log_fn("CipherKey HEX        : " + " ".join(to_hex(b) for b in text_to_bytes(key_text)))
    log_fn("")

    # 1) Key expansion (verbose)
    round_keys = key_expansion_verbose(key_text, log_fn)

    # 2) Encrypt block with full verbose
    cipher_bytes = aes_encrypt_block_verbose(pt_bytes, round_keys, log_fn)

    cipher_hex = " ".join(to_hex(b) for b in cipher_bytes)
    try:
        cipher_ascii = "".join(chr(b) for b in cipher_bytes)
    except Exception:
        cipher_ascii = ""
    log_fn("=== CIPHER OUTPUT ===")
    log_fn("Cipher HEX  : " + cipher_hex)
    log_fn("Cipher ASCII: " + cipher_ascii)
    return cipher_hex, cipher_ascii

# ----------------- GUI -----------------
class AESApp:
    def __init__(self,root):
        self.root=root
        root.title("AES-128 Step-by-Step — FULL DETAIL (Version A)")
        root.geometry("1200x760")
        root.configure(bg="#111216")

        header=tk.Frame(root,bg="#0f1720")
        header.pack(fill="x",pady=(8,12))
        tk.Label(header,text="Kriptografi dengan AES)",
                 bg="#0f1720",fg="#E6F7FF",font=("Segoe UI",14,"bold")).pack(padx=10,pady=8)

        main=tk.Frame(root,bg="#111216")
        main.pack(fill="both",expand=True,padx=10,pady=6)

        # left input
        left=tk.Frame(main,bg="#0f1518")
        left.pack(side="left",fill="y",padx=(0,10),pady=6)

        tk.Label(left,text="Plaintext (<=16 chars):",bg="#0f1518",fg="#DDECF6").pack(anchor="w",padx=12,pady=(8,2))
        self.entry_pt=ttk.Entry(left,width=30,font=("Consolas",11)); self.entry_pt.pack(padx=12,pady=(0,8))
        tk.Label(left,text="Cipher Key (<=16 chars):",bg="#0f1518",fg="#DDECF6").pack(anchor="w",padx=12,pady=(8,2))
        self.entry_key=ttk.Entry(left,width=30,font=("Consolas",11)); self.entry_key.pack(padx=12,pady=(0,8))

        btn_frame=tk.Frame(left,bg="#0f1518"); btn_frame.pack(padx=12,pady=10)
        style_btn={"font":("Segoe UI",10,"bold"),"width":22}
        tk.Button(btn_frame,text="Encrypt (Full Detail)",bg="#0984e3",fg="white",command=self.on_encrypt,**style_btn).grid(row=0,column=0,pady=6)
        tk.Button(btn_frame,text="Clear Log",bg="#6c6f73",fg="white",command=self.clear_log,**style_btn).grid(row=1,column=0,pady=6)
        tk.Button(btn_frame,text="Save Log",bg="#b77df6",fg="white",command=self.on_save,**style_btn).grid(row=2,column=0,pady=6)

        # right log and results
        right=tk.Frame(main,bg="#0b0e11"); right.pack(side="left",fill="both",expand=True)
        tk.Label(right,text="Process Log (Key Expansion then Encryption steps):",bg="#0b0e11",fg="#cfeef2").pack(anchor="w",padx=8,pady=(8,0))
        self.txt_log=scrolledtext.ScrolledText(right,width=90,height=34,bg="#041018",fg="#BFF3D6",insertbackground="white",font=("Consolas",10))
        self.txt_log.pack(fill="both",expand=True,padx=8,pady=6)

        result=tk.Frame(right,bg="#0b0e11"); result.pack(fill="x",padx=8,pady=(0,8))
        tk.Label(result,text="Ciphertext (HEX):",bg="#0b0e11",fg="#AEE8FF").grid(row=0,column=0,sticky="w")
        self.lbl_hex=tk.Label(result,text="",bg="#0b0e11",fg="#00e6ff",font=("Consolas",10,"bold")); self.lbl_hex.grid(row=0,column=1,sticky="w",padx=8)
        tk.Label(result,text="Ciphertext (ASCII):",bg="#0b0e11",fg="#AEE8FF").grid(row=1,column=0,sticky="w")
        self.lbl_ascii=tk.Label(result,text="",bg="#0b0e11",fg="#ffd36b",font=("Consolas",10,"bold")); self.lbl_ascii.grid(row=1,column=1,sticky="w",padx=8)

    # log helper (NO timestamp)
    def log(self, line=""):
        self.txt_log.insert(tk.END, line + "\n")
        self.txt_log.see(tk.END)

    def clear_log(self):
        self.txt_log.delete("1.0", tk.END)
        self.lbl_hex.config(text="")
        self.lbl_ascii.config(text="")

    def on_save(self):
        txt = self.txt_log.get("1.0", tk.END).strip()
        if not txt:
            messagebox.showwarning("Warning", "Log masih kosong.")
            return
        fn = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File","*.txt")])
        if fn:
            with open(fn, "w", encoding="utf-8") as f:
                f.write(txt)
            messagebox.showinfo("Saved", f"Log disimpan ke:\n{fn}")

    def on_encrypt(self):
        pt = self.entry_pt.get()
        key = self.entry_key.get()
        if not pt or not key:
            messagebox.showerror("Error", "Plaintext dan Key wajib diisi.")
            return
        self.clear_log()
        try:
            cipher_hex, cipher_ascii = aes_encrypt_full_verbose(pt, key, self.log)
            self.lbl_hex.config(text=cipher_hex)
            self.lbl_ascii.config(text=cipher_ascii)
            self.log("\nEncryption complete.")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

# ----------------- MAIN -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AESApp(root)
    root.mainloop()
