import json
import os

STUDENT_FILE = "school/students.json"
TEACHER_FILE = "school/teachers.json"

def show_report():
    students, teachers = [], []
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as f:
            students = json.load(f)
    if os.path.exists(TEACHER_FILE):
        with open(TEACHER_FILE, "r") as f:
            teachers = json.load(f)

    print("\n===== SCHOOL REPORT =====")
    print(f"Total Students: {len(students)}")
    print(f"Total Teachers: {len(teachers)}")
    print("==========================")
