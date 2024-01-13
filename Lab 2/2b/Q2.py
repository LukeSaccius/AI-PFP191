def q2_program():
    from math import gcd
    import sympy

    def find_prime_dividers(n):
        return [p for p in sympy.primerange(1, n + 1) if n % p == 0]

    def find_lcm(m, n):
        return abs(m * n) // gcd(m, n)

    def input_integer(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    m = input_integer("Enter the first integer number (m): ")
    n = input_integer("Enter the second integer number (n): ")

    m_prime_dividers = find_prime_dividers(m)
    n_prime_dividers = find_prime_dividers(n)
    common_prime_dividers = list(set(m_prime_dividers).intersection(n_prime_dividers))
    gcd_value = gcd(m, n)
    lcm_value = find_lcm(m, n)

    print(f"Common prime dividers of {m} and {n}:", common_prime_dividers)
    print(f"GCD of {m} and {n}:", gcd_value)
    print(f"LCM of {m} and {n}:", lcm_value)

q2_program()
