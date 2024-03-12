def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def question1():
    sequence = input("Enter a sequence of positive integers, separated by spaces: ")
    sequence = list(map(int, sequence.strip().split()))

    # Check if all numbers are positive
    if not all(num > 0 for num in sequence):
        print("All numbers must be positive integers.")
        return

    prime_numbers = [num for num in sequence if is_prime(num)]
    if prime_numbers:
        largest_prime = max(prime_numbers)
        print("Prime numbers in the sequence:", prime_numbers)
        print("The largest prime number:", largest_prime)
    else:
        print("There are no prime numbers in the sequence.")

question1()
