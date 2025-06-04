students = [{"roll_no": "1", "name": "goutam", "marks": 56},
            {"roll_no": "2", "name": "haha", "marks": 76},
            {"roll_no": "3", "name": "hehe", "marks": 87},
            {"roll_no": "4", "name": "kar", "marks": 54},
            {"roll_no": "5", "name": "car", "marks": 87}]


def add_student(students):
    name = input("Enter student name: ")
    roll_no = input("Enter roll_no number: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "roll_no": roll_no, "marks": marks})
    print("Student added successfully.")


def view_students(students):
    if not students:
        print("No students found.")
        return
    print("\nList of Students:")
    for idx, s in enumerate(students, 1):
        print(f"{idx}.Name:{s['name']},roll_no:{s['roll_no']},marks:{s['marks']}")


def search_student(students):
    roll_no = input("Enter roll_no number to search: ")
    found = False
    for s in students:
        if s['roll_no'] == roll_no:
            print(f"Found: Name: {s['name']}, roll_no: {s['roll_no']}, marks: {s['marks']}")
            found = True
            break
    if not found:
        print("Student not found.")


def delete_student(students):
    roll_no = input("Enter roll_no number to delete: ")
    for i, s in enumerate(students):
        if s['roll_no'] == roll_no:
            del students[i]
            print("Student deleted.")
            return
    print("Student not found.")


while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
