import json
import os

FILE = "school/teachers.json"

def assign_teacher(name, subject):
    data = []
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append({"name": name, "subject": subject})

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Teacher '{name}' assigned to {subject}.")

def show_teachers():
    if not os.path.exists(FILE):
        print("No teachers found.")
        return
    with open(FILE, "r") as f:
        data = json.load(f)
    print("\n--- Teacher List ---")
    for t in data:
        print(f"{t['name']} - {t['subject']}")
