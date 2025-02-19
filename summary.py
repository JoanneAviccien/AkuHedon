from expense import load_expenses
from read import read_expenses

def summary_expenses(bln, thn, kategori, filename="expenses.csv"):
    try:
        expenses = load_expenses(filename)
        category_total = 0
        whole_total = 0
        current_expenses = []
        for expense in expenses:
            whole_total += expense["jumlah"]
            if expense["tanggal"][0:4] == thn:
                if int(expense["tanggal"][5:7]) == int(bln):
                    if expense["kategori"] == kategori:
                        current_expenses.append(expense)
                        category_total += expense["jumlah"]
        read_expenses(current_expenses)
        return  category_total, round(category_total / whole_total * 100, 2)
    except:
        print("DATA TIDAK DITEMUKAN")