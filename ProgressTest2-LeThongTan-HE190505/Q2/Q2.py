class Employee:
    def __init__(self, code, name, salary, allowance):
        self.code = code
        self.name = name.strip()  # Strip any whitespace
        self.salary = float(salary)
        self.allowance = float(allowance)
    
    def total_compensation(self):
        return self.salary + self.allowance
    
    def __repr__(self):
        return f"{self.code}, {self.name}, {self.salary}, {self.allowance}"

def add_employee(employees, code, name, salary, allowance):
    employees.append(Employee(code, name, salary, allowance))
    employees.sort(key=lambda e: e.name.lower())  # Sort by name for binary search, case-insensitive
    with open('input.txt', 'w') as file:
        for emp in employees:
            file.write(f"{emp}\n")

def find_employee_by_name(employees, name):
    name = name.strip().lower()  # Prepare the name for case-insensitive comparison
    employees.sort(key=lambda e: e.name.lower())  # Sort by name for binary search, case-insensitive
    left, right = 0, len(employees) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_name = employees[mid].name.lower()  # Compare names in lowercase
        if mid_name == name:
            return employees[mid]
        elif mid_name < name:
            left = mid + 1
        else:
            right = mid - 1
    return None

def remove_employee_by_code(employees, code):
    employees[:] = [emp for emp in employees if emp.code != code]
    with open('input.txt', 'w') as file:
        for emp in employees:
            file.write(f"{emp}\n")

def print_and_save_sorted_employees_descending(employees):
    # Sort the employees in descending order by total compensation
    sorted_employees = sorted(employees, key=lambda e: e.total_compensation(), reverse=True)
    
    # Print the sorted list to the console
    print("Sorted employees (descending by total compensation):")
    for emp in sorted_employees:
        print(emp)
    
    # Save the sorted list to 'result.txt'
    with open('result.txt', 'w') as file:
        for emp in sorted_employees:
            file.write(f"{emp}\n")

def load_employees_from_file():
    employees = []
    with open('input.txt', 'r') as file:
        for line in file:
            code, name, salary, allowance = line.split(', ')
            employees.append(Employee(code, name, salary, allowance))
    return employees

# Main program starts here
employees = load_employees_from_file()

while True:
    print("1. Add a new employee")
    print("2. Find an employee by name")
    print("3. Remove an employee by code")
    print("4. Print and save list in descending order of salary + allowance")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        code = input("Enter employee code: ")
        name = input("Enter employee name: ")
        salary = input("Enter employee salary: ")
        allowance = input("Enter employee allowance: ")
        add_employee(employees, code, name, salary, allowance)
    elif choice == '2':
        name = input("Enter the name to search for: ")
        employee = find_employee_by_name(employees, name)
        if employee:
            print("Employee found:", employee)
        else:
            print("Employee not found.")
    elif choice == '3':
        code = input("Enter the employee code to remove: ")
        remove_employee_by_code(employees, code)
        print("Employee removed if existed.")
    elif choice == '4':
        print_and_save_sorted_employees_descending(employees)
        print("Employees list printed and saved in descending order.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
