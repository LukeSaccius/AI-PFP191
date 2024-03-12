import random

class employee:
    id = ''
    name = ''
    salary = 0
    age = 0

    def inputEmployee(self):
        self.id = int(input('Enter employee\'s '))
        self.name = input('Enter name: ')
        self.salary = int(input('Enter salary: '))
        self.age = int(input('Enter age: '))

    def printEmployee(self):
        print('Employee', self.id)
        print(self.name)
        print(self.salary)
        print(self.age)

class Main:
    def InputListEmployee(self):
        n = int(input('Enter the number of employees: '))
        lst = []
        for i in range(n):
            e = employee()
            e.inputEmployee()
            lst.append(e)
        return lst

    def f1(self):
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        for x in employeeList:
            x.printEmployee()

    def f2(self):
        employeeList = self.InputListEmployee()
        employeeList.sort(key=lambda x: x.age, reverse=True)
        print("OUTPUT")
        for x in employeeList:
            x.printEmployee()

    def f3(self):
        employeeList = self.InputListEmployee()
        print("OUTPUT")
        lst = []
        for x in employeeList:
            if x.age > 18: lst.append(x)
        lst.sort(key=lambda x: x.salary, reverse=True)
        for x in lst:
            x.printEmployee()

    def main(self):
        print("1. Test f1 (1 mark)")
        print("2. Test f2 (2 mark)")
        print("3. Test f3 (1 mark)")
        print("Your selection (1 -> 3): ")
        choice = int(input())
        if choice == 1:
            self.f1()
        elif choice == 2:
            self.f2()
        elif choice == 3:
            self.f3()
        else:
            print("Wrong select")
        print("FINISH")

main = Main()
main.main()
