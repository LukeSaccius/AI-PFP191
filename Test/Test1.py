def find_missing(n, numbers):
    return n * (n + 1) // 2 - sum(numbers)

try:
    n = int(input('Enter n: '))
    numbers = list(map(int, input(f'Enter {n - 1} numbers: ').split()))
    missing = find_missing(n, numbers)
    print(f'Missing value: {missing}')
except ValueError:
    print("Invalid input.")
