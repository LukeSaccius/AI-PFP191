def get_alphabetic_grade(decimal_grade):
    if decimal_grade >= 9:
        return "A+"
    elif decimal_grade >= 8:
        return "A"
    elif decimal_grade >= 7:
        return "B"
    elif decimal_grade >= 6:
        return "C"
    elif decimal_grade >= 5:
        return "D"
    else:
        return "F"

def get_4th_system_grade(decimal_grade):
    # This grading system is based on the provided link's mapping.
    # Modify the ranges and return values as needed to match your specific grading system.
    if decimal_grade >= 8.5:
        return "4.0"
    elif decimal_grade >= 8:
        return "3.7"
    elif decimal_grade >= 7:
        return "3.0"
    elif decimal_grade >= 6:
        return "2.0"
    elif decimal_grade >= 5:
        return "1.0"
    else:
        return "0.0"

# Example usage with input validation:
while True:
    try:
        grade = float(input("Enter the grade of a subject in decimal system: "))
        alpha_grade = get_alphabetic_grade(grade)
        system4_grade = get_4th_system_grade(grade)
        print(f"Corresponding alphabetic grade: {alpha_grade}")
        print(f"Corresponding 4th system grade: {system4_grade}")
        break
    except ValueError:
        print("Please enter a valid decimal number for the grade.")
