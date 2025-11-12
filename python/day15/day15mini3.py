class OutOfStockError(Exception):
    pass

store = {
    "Laptop": {"price": 60000, "stock": 5},
    "Phone": {"price": 30000, "stock": 8},
    "Headphones": {"price": 2000, "stock": 15}
}

cart = {}

def add_to_cart(item, quantity):
    if item not in store:
        raise KeyError("Product not found in store.")
    if quantity > store[item]["stock"]:
        raise OutOfStockError("Not enough stock available.")
    store[item]["stock"] -= quantity
    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {"price": store[item]["price"], "quantity": quantity}

def remove_from_cart(item):
    if item in cart:
        store[item]["stock"] += cart[item]["quantity"]
        del cart[item]
    else:
        raise KeyError("Item not found in cart.")

def view_cart():
    if not cart:
        print("🛒 Your cart is empty.")
    else:
        print("\nItems in your cart:")
        total = 0
        for item, details in cart.items():
            cost = details["price"] * details["quantity"]
            print(f"{item}: {details['quantity']} × ₹{details['price']} = ₹{cost}")
            total += cost
        print(f"Total: ₹{total}")

def checkout():
    if not cart:
        print("Cart is empty. Add items before checkout.")
        return
    total = sum(details["price"] * details["quantity"] for details in cart.values())
    print(f"Total amount to pay: ₹{total}")
    try:
        payment = float(input("Enter payment amount: ₹"))
        if payment < total:
            raise ValueError("Insufficient payment amount.")
        print("✅ Payment successful! Thank you for shopping.")
        cart.clear()
    except ValueError as e:
        print(f"⚠️ {e}")

def main():
    while True:
        print("\n1. Add to Cart\n2. Remove from Cart\n3. View Cart\n4. Checkout\n5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                item = input("Enter product name: ").title()
                qty = int(input("Enter quantity: "))
                add_to_cart(item, qty)
                print(f"✅ {qty} {item}(s) added to cart.")
            elif choice == 2:
                item = input("Enter product name to remove: ").title()
                remove_from_cart(item)
                print(f"🗑️ {item} removed from cart.")
            elif choice == 3:
                view_cart()
            elif choice == 4:
                checkout()
            elif choice == 5:
                print("👋 Thank you for visiting!")
                break
            else:
                print("⚠️ Invalid choice.")
        except ValueError:
            print("⚠️ Please enter a numeric value.")
        except KeyError as e:
            print(f"🚫 Error: {e}")
        except OutOfStockError as e:
            print(f"🚫 Error: {e}")

if __name__ == "__main__":
    main()
