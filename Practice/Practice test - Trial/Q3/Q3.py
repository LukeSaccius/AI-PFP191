class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def __str__(self):
        return f"{self.name}\n{self.salary}\n{self.age}"

class Main:
    def input_list_employee(self):
        number_of_employees = int(input("Enter the number of employees: "))
        employees = []
        for i in range(number_of_employees):
            print(f"Enter employee {i + 1}")
            name = input("Enter name: ")
            salary = int(input("Enter salary: "))
            age = int(input("Enter age: "))
            employees.append(Employee(name, salary, age))
        return employees

    def print_employees(self, employees):
        for i, employee in enumerate(employees, start=1):
            print(f"Employee {i}")
            print(employee)

    def f1(self, employees):
        print("OUTPUT")
        self.print_employees(employees)

    def f2(self, employees):
        employees.sort(key=lambda e: e.age, reverse=True)
        print("OUTPUT")
        self.print_employees(employees)

    def f3(self, employees):
        employees_over_18 = [e for e in employees if e.age >= 18]
        employees_over_18.sort(key=lambda e: e.salary, reverse=True)
        print("OUTPUT")
        self.print_employees(employees_over_18)

    def main_menu(self):
        print("1. Test f1 (1 mark)")
        print("2. Test f2 (2 marks)")
        print("3. Test f3 (1 mark)")
        selection = input("Your selection (1 -> 3): ")
        return selection

    def main(self):
        selection = self.main_menu()
        employees = self.input_list_employee()
        if selection == '1':
            self.f1(employees)
        elif selection == '2':
            self.f2(employees)
        elif selection == '3':
            self.f3(employees)
        else:
            print("Invalid selection.")
        print("FINISH")

# Create an instance of the Main class and call the main method
main_instance = Main()
main_instance.main()
