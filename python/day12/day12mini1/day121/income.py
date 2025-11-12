import json
import os
from datetime import datetime

FILE_PATH = "finance/income_data.json"

def add_income(amount, source):
    """Add income entry."""
    income_entry = {
        "amount": amount,
        "source": source,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    data = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
    data.append(income_entry)
    
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
    print("Income added successfully!")

def get_total_income():
    """Calculate total income."""
    if not os.path.exists(FILE_PATH):
        return 0
    with open(FILE_PATH, "r") as f:
        data = json.load(f)
    return sum(item["amount"] for item in data)
