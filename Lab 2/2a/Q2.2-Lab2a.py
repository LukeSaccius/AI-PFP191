# Task 2: Define an outer function that includes an inner function for addition
def outer_fun(a, b):
    # Inner function to calculate the sum of a and b
    def inner_fun():
        return a + b
    
    # Add 5 to the result of the inner function and return it
    return inner_fun() + 5

# Testing Task 2 with inputs from the user
try:
    a = int(input("Enter the first number for addition: "))
    b = int(input("Enter the second number for addition: "))
    result = outer_fun(a, b)
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input. Please enter numbers.")
    