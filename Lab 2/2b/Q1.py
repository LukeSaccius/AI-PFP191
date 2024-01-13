def q1_program():
    def input_number():
        while True:
            try:
                n = int(input("Enter an integer greater than 5: "))
                if n > 5:
                    return n
                else:
                    print("Number is not greater than 5, please re-enter.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def calculate_sum(n):
        return sum(range(1, n + 1))

    def calculate_factorial(n):
        if n == 0:
            return 1
        else:
            return n * calculate_factorial(n - 1)

    def calculate_harmonic_sum(n):
        return sum(1.0 / i for i in range(1, n + 1))

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    n = input_number()
    print(f"S1 (Sum from 1 to {n}):", calculate_sum(n))
    print(f"S2 (Factorial of {n}):", calculate_factorial(n))
    print(f"S3 (Harmonic sum of {n}):", calculate_harmonic_sum(n))
    
    # Re-input for prime check without function reuse
    while True:
        try:
            prime_check = int(input("Re-enter n to check if it is a prime number: "))
            print(f"Is {prime_check} a prime number?", is_prime(prime_check))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

q1_program()
