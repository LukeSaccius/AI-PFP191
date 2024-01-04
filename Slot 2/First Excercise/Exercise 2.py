def get_input(prompt):
    while True:
        try:
            # Try to convert the input to a float
            return float(input(prompt))
        except ValueError:
            # If conversion to float fails, prompt the user to enter a valid number
            print("Please enter a numeric value.")

# Prompt the user for hours and rate, using the get_input function
hours = get_input("Enter Hours: ")
rate = get_input("Enter Rate: ")

# Calculate the gross pay
pay = hours * rate

# Print the gross pay
print("Pay:", pay)
