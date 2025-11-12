class InvalidMarksError(Exception):
    pass

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

def main():
    try:
        marks = float(input("Enter your marks: "))
        grade = calculate_grade(marks)
        print(f"✅ Your Grade: {grade}")
    except ValueError:
        print("⚠️ Invalid input! Please enter a numeric value.")
    except InvalidMarksError as e:
        print(f"🚫 Error: {e}")

if __name__ == "__main__":
    main()
