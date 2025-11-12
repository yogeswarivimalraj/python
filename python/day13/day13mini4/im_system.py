class Product:
    def __init__(self, name, price, quantity):
        self.__name = name           # private attribute (Encapsulation)
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def update_quantity(self, qty):
        self.__quantity += qty  # Can be +ve (add stock) or -ve (reduce stock)

    def __str__(self):
        return f"📦 {self.__name} | 💰 Price: ₹{self.__price} | Qty: {self.__quantity}"


class Inventory:
    def __init__(self):
        self.__products = {}     # Encapsulated inventory
        self.__total_earnings = 0.0

    # Add a new product or update existing
    def add_product(self, name, price, quantity):
        name = name.title()
        if name in self.__products:
            self.__products[name].update_quantity(quantity)
            print(f"✅ Updated stock for {name}: +{quantity} units.")
        else:
            self.__products[name] = Product(name, price, quantity)
            print(f"✅ Added new product: {name} (₹{price}) x {quantity}")

    # Purchase product (Method Overriding concept)
    def purchase_product(self, name, quantity):
        name = name.title()
        if name not in self.__products:
            print(f"❌ Product '{name}' not found!")
            return

        product = self.__products[name]
        if product.get_quantity() >= quantity:
            product.update_quantity(-quantity)
            cost = quantity * product.get_price()
            self.__total_earnings += cost
            print(f"🛒 Purchased {quantity} x {name} for ₹{cost}")
        else:
            print(f"⚠️ Only {product.get_quantity()} units of '{name}' available!")

    # Show available stock
    def show_inventory(self):
        if not self.__products:
            print("📭 No products in inventory.")
        else:
            print("\n=== 🏪 Available Stock ===")
            for product in self.__products.values():
                print(product)
            print("==========================")

    # Show total earnings
    def show_earnings(self):
        print(f"💰 Total Earnings: ₹{self.__total_earnings}")


# Main application (Abstraction)
class StoreSystem(Inventory):
    def __init__(self):
        super().__init__()

    # Run the menu system
    def run(self):
        print("🏬 Welcome to Inventory Management System")
        while True:
            print("\n========= MENU =========")
            print("1. Add Product")
            print("2. Purchase Product")
            print("3. View Inventory")
            print("4. View Total Earnings")
            print("5. Exit")
            print("========================")

            choice = input("Enter your choice (1–5): ").strip()

            if choice == "1":
                name = input("Enter product name: ")
                try:
                    price = float(input("Enter product price: "))
                    quantity = int(input("Enter quantity: "))
                    self.add_product(name, price, quantity)
                except ValueError:
                    print("⚠️ Invalid input. Please enter numbers for price/quantity.")

            elif choice == "2":
                name = input("Enter product name: ")
                try:
                    quantity = int(input("Enter quantity to purchase: "))
                    self.purchase_product(name, quantity)
                except ValueError:
                    print("⚠️ Quantity must be a number.")

            elif choice == "3":
                self.show_inventory()

            elif choice == "4":
                self.show_earnings()

            elif choice == "5":
                print("👋 Exiting... Thank you for using the system!")
                break

            else:
                print("⚠️ Invalid choice! Please enter a number between 1–5.")


# Run the system
if __name__ == "__main__":
    store = StoreSystem()
    store.run()
