from expense import load_expenses
from read import read_expenses
from update import update_expense
from input import input_handler

# program utama
expenses = load_expenses()

read_expenses(expenses)

no = input_handler("masukkan nomor: ")
tanggal = input_handler("masukkan tanggal baru: ")
jumlah = input_handler("masukkan jumlah baru (Rp): ")
kategori = input_handler("masukkan kategori baru: ")
deskripsi = input_handler("masukkan deskripsi baru: ")

update_expense(int(no), tanggal, jumlah, kategori, deskripsi)