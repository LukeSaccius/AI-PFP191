def remove_middle_if_even(n, numbers):
    if n % 2 == 0:
        middle_index = n // 2
        numbers.pop(middle_index)  # Remove the middle element if n is even
    return numbers

n = int(input('Enter n: '))
input_numbers = list(map(int, input(f'Enter {n} numbers: ').split()))
result = remove_middle_if_even(n, input_numbers)
print(result)
