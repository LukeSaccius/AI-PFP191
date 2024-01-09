# Grading system for a subject
score = float(input("Enter the score for the subject: "))

# Grading system for theory subject
if score >= 9:
    print("Grade is A+.")
elif score >= 8:
    print("Grade is A.")
elif score >= 7:
    print("Grade is B.")
elif score >= 6:
    print("Grade is C.")
elif score >= 5:
    print("Grade is D.")
else:
    print("Grade is F.")

# Grading system for practice subject (assuming the code below is for a different grading system)
if score >= 8.5:
    print("Grade is A+.")
elif score >= 7:
    print("Grade is A.")
elif score >= 6:
    print("Grade is B.")
elif score >= 5:
    print("Grade is C.")
elif score >= 4:
    print("Grade is D.")
else:
    print("Grade is F.")
