from school.students import register_student, show_students
from school.teachers import assign_teacher, show_teachers
from school.subjects import show_report

def menu():
    while True:
        print("\n--- School Management System ---")
        print("1. Register Student")
        print("2. Show Students")
        print("3. Assign Teacher")
        print("4. Show Teachers")
        print("5. School Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            sid = input("Enter student ID: ")
            register_student(name, age, sid)
        elif choice == "2":
            show_students()
        elif choice == "3":
            name = input("Enter teacher name: ")
            subject = input("Enter subject: ")
            assign_teacher(name, subject)
        elif choice == "4":
            show_teachers()
        elif choice == "5":
            show_report()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()
