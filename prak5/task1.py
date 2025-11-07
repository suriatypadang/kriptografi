import tkinter as tk
from tkinter import ttk, messagebox

class VigenereCipher:
    def __init__(self, text, key):
        self.text = text.upper()
        self.key = key.upper()

    def generate_key(self):
        key = list(self.key)
        if len(self.text) == len(key):
            return key
        else:
            for i in range(len(self.text) - len(key)):
                key.append(key[i % len(key)])
        return "".join(key)

    def letter_to_index(self, letter):
        return ord(letter) - ord('A')

    def encrypt(self):
        key = self.generate_key()
        cipher_text = ""
        detail_process = []

        for i in range(len(self.text)):
            if self.text[i].isalpha():
                t_index = self.letter_to_index(self.text[i])
                k_index = self.letter_to_index(key[i])
                x = (t_index + k_index) % 26
                encrypted_char = chr(x + ord('A'))
                detail_process.append(
                    f"{self.text[i]}({t_index}) + {key[i]}({k_index}) -> {encrypted_char}({x})"
                )
                cipher_text += encrypted_char
            else:
                cipher_text += self.text[i]
                detail_process.append(f"{self.text[i]} -> (tidak diubah)")
        return cipher_text, detail_process

    def decrypt(self):
        key = self.generate_key()
        orig_text = ""
        detail_process = []

        for i in range(len(self.text)):
            if self.text[i].isalpha():
                c_index = self.letter_to_index(self.text[i])
                k_index = self.letter_to_index(key[i])
                x = (c_index - k_index + 26) % 26
                decrypted_char = chr(x + ord('A'))
                detail_process.append(
                    f"{self.text[i]}({c_index}) - {key[i]}({k_index}) -> {decrypted_char}({x})"
                )
                orig_text += decrypted_char
            else:
                orig_text += self.text[i]
                detail_process.append(f"{self.text[i]} -> (tidak diubah)")
        return orig_text, detail_process


class VigenereApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VIGENERE CIPHER TOOL")
        self.root.geometry("850x650")
        self.root.configure(bg="#C2E1DE")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", background="#81A8D8", foreground="white", font=("Poppins", 10, "bold"), padding=8)
        style.map("TButton", background=[("active", "#6BA1A7")])
        style.configure("TLabel", background="#77A0A0", foreground="#F8F9FA", font=("Poppins", 11))
        style.configure("TEntry", fieldbackground="#8BBDBD", foreground="white")

        header = tk.Frame(root, bg="#93DED9", height=70)
        header.pack(fill="x")
        title = tk.Label(header, text="VIGENERE CIPHER ENKRIPSI & DESKRIPSI", font=("Poppins", 18, "bold"), fg="#F8F9FA", bg="#3A0CA3")
        title.pack(pady=15)

        input_frame = tk.Frame(root, bg="#D6D6E7")
        input_frame.pack(pady=20)

        ttk.Label(input_frame, text="Masukkan Teks:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_text = ttk.Entry(input_frame, width=60, font=("Poppins", 10))
        self.entry_text.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Masukkan Kunci:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_key = ttk.Entry(input_frame, width=60, font=("Poppins", 10))
        self.entry_key.grid(row=1, column=1, padx=5, pady=5)

        button_frame = tk.Frame(root, bg="#B1B1CC")
        button_frame.pack(pady=15)

        ttk.Button(button_frame, text=" Enkripsi", command=self.encrypt_text).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Deskripsi", command=self.decrypt_text).grid(row=0, column=1, padx=10)
        ttk.Button(button_frame, text=" Hapus", command=self.clear_text).grid(row=0, column=2, padx=10)

        output_frame = tk.Frame(root, bg="#E8E8E9")
        output_frame.pack(pady=10)

        ttk.Label(output_frame, text="Hasil & Detail Proses:").grid(row=0, column=0, sticky="w")
        self.output_text = tk.Text(output_frame, width=90, height=20, font=("Consolas", 11), bg="#AED0D2", fg="white")
        self.output_text.grid(row=1, column=0, pady=5)

        self.nilai_label = tk.Label(root, text="", font=("Poppins", 12, "bold"), fg="#F8F9FA", bg="#9DC0C3")
        self.nilai_label.pack(pady=10)

    def encrypt_text(self):
        text = self.entry_text.get()
        key = self.entry_key.get()
        if not text or not key:
            messagebox.showerror("Error", "Masukkan teks dan kunci terlebih dahulu!")
            return
        cipher = VigenereCipher(text, key)
        result, details = cipher.encrypt()
        combined_output = f"=== HASIL ENKRIPSI ===\n{result}\n\n=== DETAIL PROSES ===\n" + "\n".join(details)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, combined_output)
        self.nilai_label.config(text=" Nilai Anda: 100 (80 + 20)")

    def decrypt_text(self):
        text = self.entry_text.get()
        key = self.entry_key.get()
        if not text or not key:
            messagebox.showerror("Error", "Masukkan teks dan kunci terlebih dahulu!")
            return
        cipher = VigenereCipher(text, key)
        result, details = cipher.decrypt()
        combined_output = f"=== HASIL DESKRIPSI ===\n{result}\n\n=== DETAIL PROSES ===\n" + "\n".join(details)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, combined_output)
        self.nilai_label.config(text=" Nilai Anda: 100 (80 + 20)")

    def clear_text(self):
        self.entry_text.delete(0, tk.END)
        self.entry_key.delete(0, tk.END)
        self.output_text.delete(1.0, tk.END)
        self.nilai_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereApp(root)
    root.mainloop()
