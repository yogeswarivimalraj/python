import json
import os

class Book:
    def __init__(self, title, author, copies):
        self.title = title.title()
        self.author = author.title()
        self.copies = copies

    def __str__(self):
        return f"📘 {self.title} by {self.author} — Copies: {self.copies}"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "copies": self.copies}


class Library:
    def __init__(self, data_file="books_data.json"):
        self.books = {}
        self.data_file = data_file
        self.load_books()

    def load_books(self):
        """Load books from file if it exists."""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                try:
                    data = json.load(f)
                    for title, details in data.items():
                        self.books[title] = Book(details["title"], details["author"], details["copies"])
                except json.JSONDecodeError:
                    pass

    def save_books(self):
        """Save current books to file."""
        data = {title: book.to_dict() for title, book in self.books.items()}
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def add_book(self, title, author, copies):
        title = title.title()
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)
        self.save_books()
        print(f"✅ {copies} copy(ies) of '{title}' added successfully!")

    def borrow_book(self, title):
        title = title.title()
        if title in self.books:
            book = self.books[title]
            if book.copies > 0:
                book.copies -= 1
                self.save_books()
                print(f"📖 You borrowed '{book.title}'. Enjoy reading!")
            else:
                print(f"❌ '{book.title}' is currently unavailable.")
        else:
            print(f"⚠️ '{title}' not found in library.")

    def return_book(self, title):
        title = title.title()
        if title in self.books:
            self.books[title].copies += 1
            self.save_books()
            print(f"🔁 Thank you for returning '{title}'.")
        else:
            print(f"⚠️ '{title}' does not belong to this library.")

    def view_books(self):
        if not self.books:
            print("📚 No books available in the library.")
        else:
            print("\n=== Available Books ===")
            for book in self.books.values():
                print(book)
            print("========================")


def main():
    library = Library()
    print("🏫 Welcome to the OOP Library Management System 📚")

    while True:
        print("\n========= MENU =========")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. Exit")
        print("========================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            try:
                copies = int(input("Enter number of copies: "))
                if copies > 0:
                    library.add_book(title, author, copies)
                else:
                    print("⚠️ Number of copies must be greater than 0.")
            except ValueError:
                print("⚠️ Invalid number entered.")

        elif choice == "2":
            title = input("Enter the title to borrow: ")
            library.borrow_book(title)

        elif choice == "3":
            title = input("Enter the title to return: ")
            library.return_book(title)

        elif choice == "4":
            library.view_books()

        elif choice == "5":
            print("👋 Exiting... Thank you for using the Library System!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1–5.")


if __name__ == "__main__":
    main()
