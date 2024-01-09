def get_grade(decimal_grade, grading_scale):
    for threshold, grade in grading_scale:
        if decimal_grade >= threshold:
            return grade
    return grading_scale[-1][1]  # Return the lowest grade if no other grade matches

# Define the grading scales
alphabetic_grading_scale = [
    (9, "A+"), (8, "A"), (7, "B"), (6, "C"), (5, "D"), (0, "F")
]

fourth_system_grading_scale = [
    (8.5, "4.0"), (8, "3.7"), (7, "3.0"), (6, "2.0"), (5, "1.0"), (0, "0.0")
]

# Example usage with input validation
while True:
    try:
        grade_input = input("Enter the grade of a subject in decimal system: ")
        grade = float(grade_input)
        alpha_grade = get_grade(grade, alphabetic_grading_scale)
        system4_grade = get_grade(grade, fourth_system_grading_scale)
        print(f"Corresponding alphabetic grade: {alpha_grade}")
        print(f"Corresponding 4th system grade: {system4_grade}")
        break
    except ValueError:
        print("Please enter a valid decimal number for the grade.")
