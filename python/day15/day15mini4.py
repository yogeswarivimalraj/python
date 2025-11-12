class BookingFullError(Exception):
    pass

class RailwayReservation:
    def __init__(self):
        self.available_seats = {
            "Sleeper": 3,
            "AC": 2,
            "General": 5
        }
        self.bookings = []

    def book_ticket(self, name, destination, seat_type):
        if not name.strip().isalpha():
            raise ValueError("Invalid name. Please enter alphabets only.")
        if seat_type not in self.available_seats:
            raise IndexError("Invalid seat type selected.")
        if self.available_seats[seat_type] <= 0:
            raise BookingFullError("No seats available in this category.")
        self.available_seats[seat_type] -= 1
        ticket = {"Name": name, "Destination": destination, "Seat Type": seat_type}
        self.bookings.append(ticket)
        print(f"✅ Ticket booked successfully for {name} to {destination} ({seat_type}).")

    def cancel_ticket(self, name):
        for ticket in self.bookings:
            if ticket["Name"].lower() == name.lower():
                self.available_seats[ticket["Seat Type"]] += 1
                self.bookings.remove(ticket)
                print(f"🗑️ Ticket for {name} has been canceled.")
                return
        raise ValueError("No booking found for this name.")

    def view_tickets(self):
        if not self.bookings:
            print("🚉 No tickets booked yet.")
        else:
            print("\n📜 Booked Tickets:")
            for ticket in self.bookings:
                print(f"Name: {ticket['Name']}, Destination: {ticket['Destination']}, Seat: {ticket['Seat Type']}")

def main():
    system = RailwayReservation()
    while True:
        print("\n1. Book Ticket\n2. Cancel Ticket\n3. View Tickets\n4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter passenger name: ")
                destination = input("Enter destination: ")
                seat_type = input("Enter seat type (Sleeper/AC/General): ").title()
                system.book_ticket(name, destination, seat_type)
            elif choice == 2:
                name = input("Enter passenger name to cancel: ")
                system.cancel_ticket(name)
            elif choice == 3:
                system.view_tickets()
            elif choice == 4:
                print("👋 Thank you for using the Railway Reservation System!")
                break
            else:
                print("⚠️ Invalid choice.")
        except ValueError as e:
            print(f"🚫 Error: {e}")
        except IndexError as e:
            print(f"🚫 Error: {e}")
        except BookingFullError as e:
            print(f"🚫 Error: {e}")

if __name__ == "__main__":
    main()
