from rich.console import Console
from rich.table import Table

table = Table()
console = Console()

def read_expenses(expenses):
    table.add_column("No", justify="left", style="white")
    table.add_column("Tanggal", justify="center", style="cyan")
    table.add_column("Jumlah", justify="center", style="magenta")
    table.add_column("Kategori", justify="center", style="green")
    table.add_column("Deskripsi", justify="left",  style="green")

    i = 0
    while (i < len(expenses)):
        table.add_row(expenses[i]['no'], expenses[i]['tanggal'], "Rp " + str(expenses[i]['jumlah']), expenses[i]['kategori'], expenses[i]['deskripsi'])
        i = i + 1

    console.print(table)