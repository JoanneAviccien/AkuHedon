from rich import print
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.console import Group, Console
from expense import *
from datetime import datetime
from sys import platform
import os

def newnum():
    # Comparator
    i = 0
    j = 0
    k = 0
    temp = 0
    loadf = load_expenses("expenses.csv")
    # Mencari No. paling tinggi yang terdapat pada csv
    while (i + 1 < len(loadf)):
         j = loadf[i]['no']
         k = loadf[i + 1]['no']
         if j < k:
            temp = int(k) + 1
         i = i + 1
    return temp

def gettime():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    return date

def penambahan ():
    
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

    # Assignent nilai untuk penambahan
    no = newnum()
    jumlah = Prompt.ask("Berapa Pengeluaran anda")
    kategori = Prompt.ask("Pilih Kategori anda", choices=["makanan", "hiburan", "minuman", "transportasi", "elektronik", "kesehatan", "lainnya"])
    deskripsi = Prompt.ask("Masukan Deskripsi")
    tanggal = gettime() 
    judul = "Tambahkan Pengeluaran baru ke-" + str(no)
    saveexpense = load_expenses("expenses.csv")
    saveexpense.append({"no" : no, "tanggal" : tanggal, "jumlah" : int(jumlah), "kategori" : kategori, "deskripsi" : deskripsi})
    save_expenses(saveexpense, "expenses.csv")

    # Rekap Ulang Pengeluaran Pengguna
    displaypengeluaran = Group(
        Panel.fit("[red]Jumlah Pengeluaran anda: Rp." + jumlah),
        Panel.fit("[white]Deskripsi Pengeluaran anda:\n" + deskripsi),
        Panel.fit("[green]Kategori:\n" + kategori),
    )
    print(Panel.fit(displaypengeluaran, title=judul, subtitle="Pelacak Pengeluaran " + tanggal))
    input()
