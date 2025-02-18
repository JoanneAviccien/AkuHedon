import os.path
import time

# Fungsi untuk menampilkan splash screen sebelum munculnya tampilan menu
def splash_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar terminal
    splash_text = """
    ==========================================
    |                                         |
    |      APLIKASI PELACAK PENGELUARAN       |
    |   Kelola Pengeluaran Anda dengan mudah  |
    |                                         |
    ==========================================
    |  Developer Team : A1 Team               |
    |  Version        : 1.0                   |
    |  Loading... Please Wait                 |
    ==========================================
    """
    for line in splash_text.split("\n"):
        print(line)
        time.sleep(0.1)  # Efek loading
    time.sleep(2)  # Menampilkan splash screen selama beberapa detik
    os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar setelah splash screen

def open_file():
    path = 'Pengeluaran.txt'

    cek_file = os.path.isfile(path)

    if not cek_file:
        with open(path, "w") as file:
            file.write("0")  # Menulis angka 0 jika file belum ada
        expenses = "0"  # Karena baru ditulis, isinya pasti "0"
    else:
        with open(path, "r") as file:
            expenses = file.read().strip()  # Membaca isi file dan menghapus spasi atau newline

def display_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("""
    ==========================================
    |                                         |
    |      APLIKASI PELACAK PENGELUARAN       |
    |   Kelola Pengeluaran Anda dengan mudah  |
    |                                         |
    ==========================================
    |              Daftar Menu                |
    |                                         |
    |  1. Tambah Pengeluaran                  |
    |  2. Hapus Pengeluaran                   |
    |  3. Lihat Semua Pengeluaran             |
    |  4. Edit Pengeluaran                    |
    |  5. Saring Pengeluaran                  |
    |  6. Ringkasan Bulanan                   |
    |  7. Keluar                              |
    |                                         |
    ==========================================
    """)
    return int(input("Pilih menu: "))

# Program utama
if __name__ == "__main__":
    splash_screen()  # Tampilkan splash screen hanya sekali
    open_file()  # Cek atau buat file data

    while True:
        pilihan = display_menu()
        match pilihan:
            case 1:
                Penambahan()
            case 2:
                Pengurangan()
            case 3:
                list_pengeluaran()
            case 4:
                Edit_pengeluaran()
            case 5:
                Saring()
            case 6:
                Ringkasan()
            case 7:
                print("Terima kasih telah menggunakan aplikasi!")
                break  # Keluar dari loop