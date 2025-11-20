import random
import tkinter as tk
from tkinter import messagebox

class PermainanMatematikaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Permainan Matematika")
        self.root.geometry("400x300")

        self.jumlah_babak = 5
        self.babak_sekarang = 1
        self.skor = 0

        # Frame utama
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Label judul
        self.label_judul = tk.Label(self.frame, text="Permainan Matematika", font=("Arial", 16, "bold"))
        self.label_judul.pack(pady=10)

        # Label soal
        self.label_soal = tk.Label(self.frame, text="", font=("Arial", 14))
        self.label_soal.pack()

        # Input jawaban
        self.entry_jawaban = tk.Entry(self.frame, font=("Arial", 14), justify="center")
        self.entry_jawaban.pack(pady=5)

        # Label submit
        self.btn_submit = tk.Button(self.frame, text="Jawab", font=("Arial", 12), command=self.periksa_jawaban)
        self.btn_submit.pack(pady=5)

        # Label skor
        self.label_skor = tk.Label(self.frame, text="Skor: 0", font=("Arial", 12))
        self.label_skor.pack()

        self.buat_soal()

    def buat_soal(self):
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        operasi = random.choice(['+', '-', '*', '/'])

        if operasi == '/':
            angka1 = angka1 * angka2

        self.soal = f"{angka1} {operasi} {angka2}"

        if operasi == '+':
            self.jawaban_benar = angka1 + angka2
        elif operasi == '+':
            self.jawaban_benar = angka1 - angka2
        elif operasi == '*':
            self.jawaban_benar = angka1 * angka2
        elif operasi == '/':
            self.jawaban_benar = angka1 / angka2

        self.label_soal.config(text=f"Soal {self.babak_sekarang}: {self.soal} = ?")
        self.entry_jawaban.delete(0, tk.END)

    def periksa_jawaban(self):
        try:
            jawaban_pengguna = int(self.entry_jawaban.get())
        except ValueError:
            messagebox.showwarning("Error", "Masukan angka yang valid!")
            return
        
        if jawaban_pengguna == self.jawaban_benar:
            messagebox.showinfo("Hail", "Benar!")
            self.skor += 1
        else:
            messagebox.showinfo("Hasil", f"Salah!\nJawaban benar: {self.jawaban_benar}")

        self.label_skor.config(text=f"Skor: {self.skor}")

        self.babak_sekarang += 1

        if self.babak_sekarang > self.jumlah_babak:
            self.selesai()
        else:
            self.buat_soal()

    def selesai(self):
        pesan = f"Permainan selesai!\nSkor Anda: {self.skor}/{self.jumlah_babak}\n"

        if self.skor >= 3:
            pesan += "Selamat, Anda lulus!"
        else:
            pesan += "Belum lulus, coba lagi!"

        if self.skor == self.jumlah_babak:
            pesan += "\nAnda Lulus Ke Tahap Selanjutnya!"
        elif self.skor > self.jumlah_babak // 2:
            pesan += "\nkerja bagus! terus berlatih"
        else:
            pesan += "\nTetap semangat! Latihan membuat sempurna!"

            messagebox.showinfo("Hasil", pesan)
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PermainanMatematikaGUI(root)
    root.mainloop()