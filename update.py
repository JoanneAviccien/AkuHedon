from expense import load_expenses
from expense import save_expenses

def update_expense(no, new_tanggal, new_jumlah, new_kategori, new_deskripsi, filename="expenses.csv"):
    expenses = load_expenses(filename)
    for expense in expenses:
        if int(expense["no"]) == int(no):
            expense["tanggal"] = new_tanggal
            expense["jumlah"] = new_jumlah
            expense["kategori"] = new_kategori
            expense["deskripsi"] = new_deskripsi
    
    save_expenses(expenses)
