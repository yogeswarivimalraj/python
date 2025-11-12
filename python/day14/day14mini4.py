import csv

def add_score():
    name = input("Enter student name: ")
    subject = input("Enter subject: ")
    score = input("Enter score: ")

    with open("scores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, subject, score])

    print("✅ Score added successfully!")

def view_scores():
    try:
        with open("scores.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if not rows:
                print("📂 No scores found!")
                return

            print("\n--- All Quiz Scores ---")
            print("Name\t\tSubject\t\tScore")
            print("-" * 35)
            for row in rows:
                if len(row) == 3:
                    name, subject, score = row
                    print(f"{name}\t\t{subject}\t\t{score}")
    except FileNotFoundError:
        print("⚠️ No data file found. Please add scores first!")

def search_score():
    search_name = input("Enter student name to search: ").strip().lower()
    found = False
    try:
        with open("scores.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    name, subject, score = row
                    if name.lower() == search_name:
                        print("\n🎯 Student Found:")
                        print(f"Name: {name}\nSubject: {subject}\nScore: {score}")
                        found = True
        if not found:
            print("❌ Student not found!")
    except FileNotFoundError:
        print("⚠️ No data file found. Please add scores first!")

def main():
    while True:
        print("\n===== QUIZ SCORE MANAGER =====")
        print("1. Add Score")
        print("2. View All Scores")
        print("3. Search by Student Name")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_score()
        elif choice == "2":
            view_scores()
        elif choice == "3":
            search_score()
        elif choice == "4":
            print("💾 Exiting program... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please select 1–4.")

if __name__ == "__main__":
    main()
