class PupilRecord:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

def display_main_menu():
    print("1. REPORT MENU")
    print("2. ADMIN MENU")
    print("3. EXIT")
    
def input_integer(message):
    while True:
        try:
            value = int(input(message))
            if 0 <= value <= 10:
                return value
            else:
                print("Invalid input. Please enter a value between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# The rest of your code remains the same

############################################################ ADMIN MENU ############################################################################
def display_admin_menu():
    print("1. Create pupil record")
    print("2. Display all pupil records")
    print("3. Search pupil record")
    print("4. Modify pupil record")
    print("5. Delete pupil record")
    print("6. Back to main menu")
    
def create_pupil_record():
    while True:
        roll_number = input("Enter roll number: ")
        # Check if the roll number already exists
        if roll_number in pupils:
            print("This roll number already exists. Please enter a different roll number.")
            continue  # Skip the rest of the loop and prompt for the roll number again
        
        name = input("Enter name: ")
        marks = {
            'English': input_integer("Enter Marks in English: "),
            'Math': input_integer("Enter Marks in Maths: "),
            'Physics': input_integer("Enter Marks in Physics: "),
            'Chemistry': input_integer("Enter Marks in Chemistry: "),
            'CS': input_integer("Enter Marks in CS: ")
        }
        pupils[roll_number] = PupilRecord(roll_number, name, marks)
        more_records = input("Want to enter more record (y/n)?: ").lower()
        if more_records == 'n':
            break
        elif more_records == 'y':
            continue
        else:
            print("Invalid Choice! Please type again")


def display_all_pupil_records():
    for roll_number, pupil in pupils.items():
        print("PUPIL DETAILS..")
        print(f"Roll Number: {pupil.roll_number}")
        print(f"Name: {pupil.name}")
        print(f"English: {pupil.marks['English']}")
        print(f"Maths: {pupil.marks['Math']}")
        print(f"Physics: {pupil.marks['Physics']}")
        print(f"Chemistry: {pupil.marks['Chemistry']}")
        print(f"CS: {pupil.marks['CS']}")
        print()  # Print a blank line between records for better readability


def search_pupil_record():
    roll_number = input("Enter the roll number you want to search: ")
    pupil = pupils.get(roll_number)
    if pupil:
        print("PUPIL DETAILS..")
        print(f"Roll Number: {pupil.roll_number}")
        print(f"Name: {pupil.name}")
        print(f"English: {pupil.marks['English']}")
        print(f"Maths: {pupil.marks['Math']}")
        print(f"Physics: {pupil.marks['Physics']}")
        print(f"Chemistry: {pupil.marks['Chemistry']}")
        print(f"CS: {pupil.marks['CS']}")
    else:
        print("Pupil record not found.")

def modify_pupil_record():
    roll_number = input("Enter roll number: ")
    pupil = pupils.get(roll_number)
    if not pupil:
        print("Pupil record not found.")
        return
    
    print("MODIFY RECORD")
    print(f"Roll Number: {roll_number}")
    print(f"Name: {pupil.name}")
    
    if input("Wants to edit(y/n)?: ").lower() == 'y':
        pupil.name = input("Enter the name: ")
    
    for subject in ['English', 'Maths', 'Physics', 'Chemistry', 'CS']:
        if input(f"Wants to edit {subject} marks (y/n)?: ").lower() == 'y':
            pupil.marks[subject] = int(input(f"Enter {subject} marks: "))
    
    print("Record updated.\n")  # Print a blank line after updating the record
    
    print("PUPIL DETAILS..")
    print(f"Roll Number: {pupil.roll_number}")
    print(f"Name: {pupil.name}")
    print(f"English: {pupil.marks['English']}")
    print(f"Maths: {pupil.marks['Math']}")
    print(f"Physics: {pupil.marks['Physics']}")
    print(f"Chemistry: {pupil.marks['Chemistry']}")
    print(f"CS: {pupil.marks['CS']}")

def delete_pupil_record():
    roll_number = input("Enter roll number: ")
    pupil = pupils.get(roll_number)
    if pupil:
        print("PUPIL DETAILS..")
        print(f"Roll Number: {pupil.roll_number}")
        print(f"Name: {pupil.name}")
        print(f"English: {pupil.marks['English']}")
        print(f"Maths: {pupil.marks['Math']}")
        print(f"Physics: {pupil.marks['Physics']}")
        print(f"Chemistry: {pupil.marks['Chemistry']}")
        print(f"CS: {pupil.marks['CS']}")
        
        del pupils[roll_number]
        print("RECORD found and deleted")
    else:
        print("Record not found.")
        
def admin_menu():
    while True:
            display_admin_menu()
            admin_choice = input("Enter choice (1-6): ")
            if admin_choice == '1':
                create_pupil_record()
            elif admin_choice == '2':
                display_all_pupil_records()
            elif admin_choice == '3':
                search_pupil_record()
            elif admin_choice == '4':
                modify_pupil_record()
            elif admin_choice == '5':
                delete_pupil_record()
            elif admin_choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
############################################# REPORT MENU ###############################################
def display_report_menu():
    print("REPORT MENU")
    print("1. Class result")
    print("2. Pupil report card")
    print("3. Back to main menu")

def class_result():
    print("RollNo Name           English Maths Physics Chemistry CS")
    for roll_number, pupil in pupils.items():
        marks = pupil.marks
        print(f"{pupil.roll_number:<6} {pupil.name:<15} {marks['English']:<8} {marks['Math']:<5} {marks['Physics']:<8} {marks['Chemistry']:<9} {marks['CS']}")

def pupil_report_card():
    roll_number = input("Enter the roll number you want to search: ")
    pupil = pupils.get(roll_number)
    if pupil:
        print("PUPIL DETAILS..")
        print(f"Roll Number: {pupil.roll_number}")
        print(f"Name: {pupil.name}")
        print(f"English: {pupil.marks['English']}")
        print(f"Maths: {pupil.marks['Math']}")
        print(f"Physics: {pupil.marks['Physics']}")
        print(f"Chemistry: {pupil.marks['Chemistry']}")
        print(f"CS: {pupil.marks['CS']}")
    else:
        print("Pupil record not found.")

def report():
    while True:
        display_report_menu()
        choice = input("Enter choice (1-3): ")
        if choice == '1':
            class_result()
        elif choice == '2':
            pupil_report_card()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
#########################################################################################################

pupils = {}
while True:
    display_main_menu()
    choice = input("Enter choice (1-3): ")
    if choice == '1':
        report()
    elif choice == '2':
        admin_menu()
    elif choice == '3':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
