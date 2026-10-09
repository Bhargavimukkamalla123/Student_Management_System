students = {}


def add_student():
    roll_number = input("Enter roll number: ")

    if roll_number in students:
        print("Student already exists.")
        return

    name = input("Enter student name: ")

    try:
        marks = float(input("Enter marks out of 100: "))
    except ValueError:
        print("Please enter valid marks.")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    students[roll_number] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully.")


def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


def view_students():
    if not students:
        print("No student records available.")
        return

    for roll_number, details in students.items():
        marks = details["marks"]

        print("\nRoll Number:", roll_number)
        print("Name:", details["name"])
        print("Marks:", marks)
        print("Grade:", calculate_grade(marks))


def search_student():
    roll_number = input("Enter roll number to search: ")

    if roll_number in students:
        details = students[roll_number]

        print("Roll Number:", roll_number)
        print("Name:", details["name"])
        print("Marks:", details["marks"])
        print("Grade:", calculate_grade(details["marks"]))
    else:
        print("Student not found.")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")