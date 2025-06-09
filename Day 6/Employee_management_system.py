class Employee:
    def __init__(self, emp_id, name, department, salary):
        
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(
            f"ID: {
                self.emp_id}, Name: {
                self.name}, Department: {
                self.department}, Salary: {
                    self.salary}"
                    )


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in self.employees:
                print("Employee ID already exists.")
                return
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            salary = int(input("Enter Salary: "))
            self.employees[emp_id] = Employee(emp_id, name, department, salary)
            print("Employee added successfully.")
        except ValueError:
            print("Invalid input. Please enter correct data types.")

    def delete_employee(self):
        try:
            emp_id = int(input("Enter Employee ID to delete: "))
            if emp_id in self.employees:
                del self.employees[emp_id]
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Employee ID.")

    def update_employee(self):
        try:
            emp_id = int(input("Enter Employee ID to update: "))
            if emp_id in self.employees:
                name = input("Enter new Name (leave blank to keep current): ")
                department = input(
                    "Enter new Department (leave blank to keep current): ")
                salary_input = input(
                    "Enter new Salary (leave blank to keep current): ")
                if name:
                    self.employees[emp_id].name = name
                if department:
                    self.employees[emp_id].department = department
                if salary_input:
                    try:
                        self.employees[emp_id].salary = int(salary_input)
                    except ValueError:
                        print("Invalid salary input. Salary not updated.")
                print("Employee updated successfully.")
            else:
                print("Employee not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Employee ID.")

    def display_all(self):
        if not self.employees:
            print("No employees to display.")
        else:
            for emp in self.employees.values():
                emp.display()


if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    while True:
        print("\n1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Display All Employees")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            ems.add_employee()
        elif choice == '2':
            ems.remove_employee()
        elif choice == '3':
            ems.update_employee()
        elif choice == '4':
            ems.display_all()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
