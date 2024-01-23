# Function that accepts a variable number of arguments and prints them.
def func1(*args):
    print("Printing values")
    for x in args:
        print(x)

# Function that returns multiple values (assumed to be the sum and the difference of the inputs).
def calculation(a, b):
    return a + b, a - b

# Gather input for func1
input_args = input("Enter numbers separated by spaces for func1: ")

try:
    numbers = [int(num) for num in input_args.split()]
    func1(*numbers)
except ValueError:
    print("Please enter only numbers separated by spaces.")

# Gather input for calculation
input_numbers = input("Enter two numbers separated by a space for calculation (e.g., '40 10'): ")
try:
    a, b = [int(num) for num in input_numbers.split()]
    sum_result, diff_result = calculation(a, b)
    print(f"The sum is: {sum_result} and the difference is: {diff_result}")
except ValueError:
    print("Please enter two valid numbers separated by a space.")
except Exception as e:
    print(f"An error occurred: {e}")
