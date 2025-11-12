from day121.income import get_total_income
from day121.expense import get_total_expense

def show_summary():
    """Display financial summary."""
    income = get_total_income()
    expense = get_total_expense()
    savings = income - expense

    print("\n====== Personal Finance Summary ======")
    print(f"Total Income : ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Savings      : ₹{savings}")
    print("=====================================")
