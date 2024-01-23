def int_to_binary(integer):
    # Convert integer to binary string, remove the '0b' prefix
    return bin(integer)[2:]

def add_binary(a, b):
    # Perform addition and return both binary and integer results
    sum_int = a + b
    return int_to_binary(sum_int), sum_int

def subtract_binary(a, b):
    # Perform subtraction using two's complement and return both binary and integer results
    difference_int = a - b  # Python already handles two's complement for negative numbers
    return int_to_binary(difference_int if difference_int >= 0 else (1 << (a.bit_length() + 1)) + difference_int), difference_int

# Input integer values for A and B from the user
A = int(input("Enter an integer for A: "))
B = int(input("Enter an integer for B: "))
operation = input("Do you want to perform addition or subtraction? (Enter 'add' or 'subtract'): ").strip().lower()

# Perform the chosen operation
if operation == 'add':
    R_bin, R_int = add_binary(A, B)
    operation_name = "Addition"
elif operation == 'subtract':
    R_bin, R_int = subtract_binary(A, B)
    operation_name = "Subtraction"
else:
    raise ValueError("Invalid operation. Please enter 'add' or 'subtract'.")

print(f"{operation_name} (binary): {R_bin}, {operation_name} (integer): {R_int}")
