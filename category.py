#pip package module
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import print
from rich.panel import Panel
#local module
from expense import load_expenses

def saring():
    pertanyaan = Prompt.ask("Pilih Kategori anda", choices=["makanan", "hiburan", "minuman", "transportasi", "elektronik", "kesehatan", "lainnya"])

    loadf = load_expenses()
    sorted = []

    i = 0
    while (i < len(loadf)):
        #If ini mencari kategori berdasarkan hasil dari jawaban pengguna
        #input pengguna diambil oleh prompt.ask lalu kita bandingkan dengan database
        #jika sesuai dengan jawaban pengguna makan index akan disimpan ke list sorted
        #untuk ditampilkan
        if loadf[i]['kategori'] == pertanyaan:
            sorted.append(loadf[i])
        i = i + 1

    i = 0
    total = 0

    #Print Tampilan
    table1 = Table(title = "Pengeluaran " + pertanyaan)
    table1.add_column("Tanggal")
    table1.add_column("Jumlah")
    table1.add_column("Deskripsi")
    while(i < len(sorted)):
        table1.add_row(sorted[i]['tanggal'], "Rp " + str(sorted[i]['jumlah']), sorted[i]['deskripsi'])
        total = total + sorted[i]['jumlah']
        i = i + 1

    console = Console()
    console.print(table1)
    print(Panel.fit("Total pengeluaran anda: Rp" + str(total)))
    input()