def add_expense():
    category = input("Enter expense category: ")
    amount = input("Enter amount: ")
    date = input("Enter date (DD-MM-YYYY): ")
    with open("expenses.txt", "a") as file:
        file.write(f"{category},{amount},{date}\n")
    print("✅ Expense added successfully!")

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            records = file.readlines()
            if not records:
                print("📂 No expenses found!")
                return
            print("\n--- All Expenses ---")
            print("Category\tAmount\tDate")
            print("-" * 35)
            for record in records:
                category, amount, date = record.strip().split(",")
                print(f"{category}\t\t{amount}\t{date}")
    except FileNotFoundError:
        print("⚠️ No data file found. Add some expenses first!")

def total_expense():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    amount = parts[1]
                    try:
                        total += float(amount)
                    except ValueError:
                        pass
        print(f"\n💰 Total Expenditure: Rs.{total}")
    except FileNotFoundError:
        print("⚠️ No data file found. Please add expenses first!")

def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenditure")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("💾 Exiting... All expenses saved in 'expenses.txt'. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter 1–4.")

if __name__ == "__main__":
    main()
