import json
import os

FILE = "school/students.json"

def register_student(name, age, student_id):
    data = []
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append({"id": student_id, "name": name, "age": age})

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Student '{name}' registered successfully!")

def show_students():
    if not os.path.exists(FILE):
        print("No students found.")
        return
    with open(FILE, "r") as f:
        data = json.load(f)
    print("\n--- Student List ---")
    for s in data:
        print(f"{s['id']} - {s['name']} ({s['age']} years old)")
