import json
import os
from datetime import datetime

FILE_PATH = "finance/expense_data.json"

def add_expense(amount, category):
    """Add expense entry."""
    expense_entry = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    data = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
    data.append(expense_entry)
    
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
    print("Expense added successfully!")

def get_total_expense():
    """Calculate total expense."""
    if not os.path.exists(FILE_PATH):
        return 0
    with open(FILE_PATH, "r") as f:
        data = json.load(f)
    return sum(item["amount"] for item in data)
