def display_unique_numbers(arr):
    unique_numbers = list(set(arr))
    unique_numbers.sort()  # Sort the numbers if needed
    return unique_numbers

# Example usage with input validation:
while True:
    try:
        array_values = list(map(int, input("Enter the numbers separated by space: ").split()))
        unique_numbers = display_unique_numbers(array_values)
        print("Unique numbers in the array:", ' '.join(map(str, unique_numbers)))
        break
    except ValueError:
        print("Please enter only numbers separated by spaces.")
