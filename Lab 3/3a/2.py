def get_valid_input(prompt, expected_type):
    while True:
        try:
            if expected_type == 'list':
                return [int(item) for item in input(prompt).split()]
            elif expected_type == 'int':
                return int(input(prompt))
        except ValueError:
            print(f"Invalid input! Please enter a {'list of numbers' if expected_type == 'list' else 'single integer'}.")

# Task 1: Process list and print numbers
num_list = get_valid_input("Enter numbers separated by spaces: ", 'list')
for num in num_list:
    if num > 500: break
    if num <= 150 and num % 5 == 0: print(num)

# Task 2: Count digits of a number
single_num = get_valid_input("Enter a number to count digits: ", 'int')
print(f"Total digits: {len(str(single_num))}")

# Task 3: Print list in reverse
print("Reversed list:", *reversed(num_list))
