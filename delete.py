from expense import load_expenses
from expense import save_expenses

def delete_expense(no, filename="expenses.csv"):
    expenses = load_expenses(filename)
    new_expense = []
    for expense in expenses:
        if expense["no"] != no:
            new_expense.append(expense)
    
    save_expenses(new_expense)
