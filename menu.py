import os.path
import time
from update import update_expense
from input import input_handler
from delete import delete_expense as remove_expense
from summary import summary_expenses as all_expenses

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

def display_menu():
    print ("""
    ==========================================
    |                                         |
    |    APLIKASI PELACAK PENGELUARAN UANG    |
    |   Kelola Pengeluaran Anda dengan mudah  |
    |                                         |
    ==========================================
    |              Daftar Menu                |
    |                                         |
    |  1. Tambah Pengeluaran                  |
    |  2. Hapus Pengeluaran                   |
    |  3. Edit Pengeluaran                    |
    |  4. Saring Pengeluaran                  |
    |  5. Ringkasan Pengeluaran               |
    |  6. Keluar                              |
    |                                         |
    ==========================================
    """)

def edit_expenses():
    no = input_handler("masukkan nomor yang ada di tabel: ")
    tanggal = input_handler("masukkan tanggal baru: ")
    jumlah = input_handler("masukkan jumlah baru (Rp): ")
    kategori = input_handler("masukkan kategori baru: ")
    deskripsi = input_handler("masukkan deskripsi baru: ")

    update_expense(int(no), tanggal, jumlah, kategori, deskripsi)
    

def delete_expense():
    no = input_handler("Masukkan nomor yang ada di tabel yang anda ingin hapus: ")
    remove_expense(no)

def summary_expenses():
    kategori = input_handler("Masukkan kategori yang anda ingin lihat: ")
    bln = input_handler("Masukkan bulan yang anda ingin lihat: ")
    thn = input_handler("Masukkan tahun yang anda ingin lihat: ")

    summary = all_expenses(bln, thn, kategori)
    print("Pengeluaran untuk ", kategori," di bulan ke ", bln , " tahun ", thn, " sebanyak ", summary[0])
    print("Persentase pengeluaran bulanan di bulan ke ", bln, " tahun ", thn, "pada kategori", kategori, "sebesar", summary[1], "%")
    input_handler()
