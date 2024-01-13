def q4_program():
    def find_palindromes_in_range(m, n):
        return [number for number in range(m, n + 1) if str(number) == str(number)[::-1]]

    def input_integer(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    m = input_integer("Enter the lower bound of the range (m): ")
    n = input_integer("Enter the upper bound of the range (n): ")

    if m >= n:
        print("Invalid range. m must be less than n.")
        return

    palindromes = find_palindromes_in_range(m, n)
    print(f"Palindromic numbers between {m} and {n}:", palindromes)

q4_program()
