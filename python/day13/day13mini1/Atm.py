# atm_system.py
from getpass import getpass
from datetime import datetime

class ATMAccount:
    def __init__(self, owner, pin, balance=0.0):
        self.owner = owner
        self.pin = str(pin)
        self.balance = float(balance)
        self.history = [] 
    def authenticate(self, pin):
        return pin == self.pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._record("Deposit", amount)
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self._record("Withdraw", amount)
            return True
        return False

    def _record(self, trans_type, amount):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append((time, trans_type, amount, self.balance))

    def show_history(self):
        if not self.history:
            print("No transactions yet.")
        else:
            print("\n----- Transaction History -----")
            for time, ttype, amt, bal in self.history:
                print(f"{time} | {ttype:<10} | ₹{amt:<8.2f} | Balance: ₹{bal:<8.2f}")
            print("--------------------------------\n")


def main():
    print("🏦 Welcome to the Python ATM System 🏦")

    name = input("Enter account holder name: ")
    pin = input("Set a 4-digit PIN: ")

    while not (pin.isdigit() and len(pin) == 4):
        pin = getpass("Invalid! Enter a 4-digit PIN: ")

    try:
        balance = float(input("Enter starting balance: ₹"))
    except ValueError:
        balance = 0.0

    user = ATMAccount(name, pin, balance)
    print(f"\n✅ Account created for {user.owner} with balance ₹{user.balance:.2f}\n")

    # Login
    entered_pin =input("Enter your PIN to log in: ")
    if not user.authenticate(entered_pin):
        print("❌ Incorrect PIN. Access Denied.")
        return

    # Main Menu
    while True:
        print("\n==== ATM MENU ====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print(f"\nYour current balance is: ₹{user.check_balance():.2f}")

        elif choice == "2":
            try:
                amt = float(input("Enter amount to deposit: ₹"))
                if user.deposit(amt):
                    print(f"✅ ₹{amt:.2f} deposited successfully.")
                else:
                    print("❌ Invalid deposit amount.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "3":
            try:
                amt = float(input("Enter amount to withdraw: ₹"))
                if user.withdraw(amt):
                    print(f"✅ ₹{amt:.2f} withdrawn successfully.")
                else:
                    print("❌ Insufficient balance or invalid amount.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "4":
            user.show_history()

        elif choice == "5":
            print("💳 Thank you for using the ATM. Goodbye!")
            break

        else:
            print("⚠️ Invalid option. Please choose between 1-5.")


if __name__ == "__main__":
    main()
