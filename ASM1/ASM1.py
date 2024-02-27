class Pupil:
    def __init__(self, id, name, age, gender, form):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.form = form

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.age}\t{self.gender}\t{self.form}"

class PupilCheckingSystem:
    def __init__(self):
        self.pupils = []

    def add_pupil(self):
        id = input("Enter pupil ID: ")
        name = input("Enter pupil name: ")
        age = input("Enter pupil age: ")
        gender = input("Enter pupil gender: ")
        form = input("Enter pupil form: ")
        new_pupil = Pupil(id, name, age, gender, form)
        self.pupils.append(new_pupil)
        print("Pupil added successfully!")

    def display_pupils(self):
        print("ID\tName\tAge\tGender\tForm")
        for pupil in self.pupils:
            print(pupil)

    def search_pupil(self):
        id = input("Enter pupil ID to search: ")
        for pupil in self.pupils:
            if pupil.id == id:
                print("Pupil found:")
                print(pupil)
                return
        print("Pupil not found.")

    def modify_pupil(self):
        id = input("Enter pupil ID to modify: ")
        for pupil in self.pupils:
            if pupil.id == id:
                pupil.name = input("Enter new pupil name: ")
                pupil.age = input("Enter new pupil age: ")
                pupil.gender = input("Enter new pupil gender: ")
                pupil.form = input("Enter new pupil form: ")
                print("Pupil record updated successfully!")
                return
        print("Pupil not found.")

    def delete_pupil(self):
        id = input("Enter pupil ID to delete: ")
        for i, pupil in enumerate(self.pupils):
            if pupil.id == id:
                del self.pupils[i]
                print("Pupil record deleted successfully!")
                return
        print("Pupil not found.")

    def run(self):
        while True:
            print("\n1. Add pupil")
            print("2. Display all pupils")
            print("3. Search pupil record")
            print("4. Modify pupil record")
            print("5. Delete pupil record")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_pupil()
            elif choice == '2':
                self.display_pupils()
            elif choice == '3':
                self.search_pupil()
            elif choice == '4':
                self.modify_pupil()
            elif choice == '5':
                self.delete_pupil()
            elif choice == '6':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

# To start the system
system = PupilCheckingSystem()
system.run()
