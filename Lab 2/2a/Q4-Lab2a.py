def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_largest_number(numbers_list):
    return max(numbers_list)

def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def get_numbers_list_input(prompt):
    while True:
        try:
            input_string = input(prompt)
            number_list = [int(item) for item in input_string.split(',')]
            return number_list
        except ValueError:
            print("Please enter a valid list of numbers separated by commas.")

# Task 1: Check if the input number is a palindrome
number_to_check = get_number_input("Enter a number to check if it's a palindrome: ")
if is_palindrome(number_to_check):
    print(f"{number_to_check} is a palindrome number.")
else:
    print(f"{number_to_check} is not a palindrome number.")

# Task 2: Find the largest number in the input list
numbers_list = get_numbers_list_input("Enter a list of numbers separated by commas to find the largest one: ")
largest_number = find_largest_number(numbers_list)
print(f"The largest number in the list is: {largest_number}")
