def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    with open("students.csv", "a") as file:
        file.write(f"{name},{age},{grade}\n")
    print("✅ Student record added successfully!")

def view_students():
    try:
        with open("students.csv", "r") as file:
            records = file.readlines()
            if not records:
                print("📂 No student records found!")
                return
            print("\n--- All Student Records ---")
            print("Name\t\tAge\tGrade")
            print("-" * 30)
            for record in records:
                name, age, grade = record.strip().split(",")
                print(f"{name}\t\t{age}\t{grade}")
    except FileNotFoundError:
        print("⚠️ No data file found. Add some students first!")

def search_student():
    search_name = input("Enter student name to search: ").strip().lower()
    found = False
    try:
        with open("students.csv", "r") as file:
            for line in file:
                name, age, grade = line.strip().split(",")
                if name.lower() == search_name:
                    print("\n🎯 Student Found:")
                    print(f"Name: {name}\nAge: {age}\nGrade: {grade}")
                    found = True
                    break
        if not found:
            print("❌ Student not found!")
    except FileNotFoundError:
        print("⚠️ No data file found. Please add students first!")

def main():
    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("💾 Exiting program... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please select 1–4.")

if __name__ == "__main__":
    main()
