# Input a string from the user
input_string = input("Enter a string: ")

# Initialize counters for digits, letters, and other characters
num_digits, num_letters, num_other = 0, 0, 0

# Count characters
for char in input_string:
    if char.isdigit():
        num_digits += 1
    elif char.isalpha():
        num_letters += 1
    else:
        num_other += 1

# Print the results
print("Number of digits:", num_digits)
print("Number of letters:", num_letters)
print("Number of other characters:", num_other)
