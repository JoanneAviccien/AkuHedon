from rich.console import Console
from rich.table import Table

table = Table()
console = Console()

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

table.add_column("Tanggal", justify="center", style="cyan")
table.add_column("Jumlah", justify="center", style="magenta")
table.add_column("Kategori", justify="center", style="green")
table.add_column("Deskripsi", justify="left",  style="green")

i = 0
while (i < len(expenses)):
    table.add_row(expenses[i]['tanggal'], "Rp " + str(expenses[i]['jumlah']), expenses[i]['kategori'], expenses[i]['deskripsi'])
    i = i + 1

console.print(table)