import os.path
import time

# Fungsi untuk menampilkan splahscreen sebelum munculnya tampilan menu
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

if __name__ == "__main__":
    splash_screen()
    print("Welcome to Expense Tracker!")

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

def Display_menu():
    os.system("cls")
    Menu_text = """
    ==========================================
    |                                         |
    |      APLIKASI PELACAK PENGELUARAN       |
    |   Kelola Pengeluaran Anda dengan mudah  |
    |                                         |
    ==========================================
    |                  Menu                   |
    |  1.                   |
    |  Loading... Please Wait                 |
    ==========================================
    """
    

while(True):

    splash_screen()
    open_file()
    Displa

    expenses = [
        {"tanggal": "2025-02-01", "jumlah": 50000, "kategori": "makanan", "deskripsi": "Sarapan nasi goreng"},
        {"tanggal": "2025-02-01", "jumlah": 15000, "kategori": "transportasi", "deskripsi": "Ojek ke kantor"},
        {"tanggal": "2025-02-02", "jumlah": 200000, "kategori": "belanja", "deskripsi": "Belanja bulanan di supermarket"},
        {"tanggal": "2025-02-02", "jumlah": 75000, "kategori": "hiburan", "deskripsi": "Nonton film di bioskop"},
        {"tanggal": "2025-02-03", "jumlah": 10000, "kategori": "minuman", "deskripsi": "Kopi susu di warung"},
        {"tanggal": "2025-02-04", "jumlah": 55000, "kategori": "makanan", "deskripsi": "Makan siang di warteg"},
        {"tanggal": "2025-02-05", "jumlah": 30000, "kategori": "transportasi", "deskripsi": "Bensin motor"},
        {"tanggal": "2025-02-06", "jumlah": 120000, "kategori": "kesehatan", "deskripsi": "Beli vitamin"},
        {"tanggal": "2025-02-07", "jumlah": 20000, "kategori": "minuman", "deskripsi": "Beli boba"},
        {"tanggal": "2025-02-08", "jumlah": 80000, "kategori": "hiburan", "deskripsi": "Langganan Netflix"},
        {"tanggal": "2025-02-09", "jumlah": 250000, "kategori": "elektronik", "deskripsi": "Beli headset baru"},
        {"tanggal": "2025-02-10", "jumlah": 100000, "kategori": "belanja", "deskripsi": "Baju baru"},
        {"tanggal": "2025-02-11", "jumlah": 45000, "kategori": "makanan", "deskripsi": "Makan malam di kafe"},
        {"tanggal": "2025-02-12", "jumlah": 20000, "kategori": "transportasi", "deskripsi": "Bus ke kampus"},
        {"tanggal": "2025-02-13", "jumlah": 30000, "kategori": "edukasi", "deskripsi": "Beli buku pemrograman"},
        {"tanggal": "2025-02-14", "jumlah": 150000, "kategori": "kesehatan", "deskripsi": "Konsultasi dokter"},
    ]


    print(expenses[0]['jumlah']) # menampilkan 'jumlah' pengeluaran yang ada di index '0'
    # print : 50000

    i = 0
    panjang_list = len(expenses)
    """ while (i < panjang_list):
        print(expenses[i])
        i = i + 1 """

    i = 0
    panjang_list = len(expenses)
    while (i < panjang_list):
        print("tanggal   : " + expenses[i]['tanggal'])
        print("jumlah    : " + f"Rp {expenses[i]['jumlah']}")
        print("kategori  : " + expenses[i]['kategori'])
        print("deskripsi : " + expenses[i]['deskripsi'])
        print("\n") # enter
        i = i + 1

