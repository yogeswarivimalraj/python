class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def check_balance(self):
        print(f"💰 Current Balance: Rs.{self.balance:.2f}")

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
            print(f"✅ Rs.{amount:.2f} deposited successfully.")
        except ValueError as e:
            print(f"⚠️ Invalid deposit amount: {e}")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance for this transaction.")
            self.balance -= amount
            print(f"✅ Rs.{amount:.2f} withdrawn successfully.")
        except ValueError as e:
            print(f"⚠️ Invalid withdrawal amount: {e}")
        except InsufficientBalanceError as e:
            print(f"🚫 Transaction failed: {e}")

def main():
    account = BankAccount(5000)
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = input("Enter amount to deposit: ")
            account.deposit(amount)
        elif choice == "3":
            amount = input("Enter amount to withdraw: ")
            account.withdraw(amount)
        elif choice == "4":
            print("💾 Exiting... Thank you for using our ATM!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1–4.")

if __name__ == "__main__":
    main()
