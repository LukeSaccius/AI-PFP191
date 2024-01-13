def q3_program():
    def input_and_validate():
        while True:
            try:
                n = int(input("Enter an integer number: "))
                return n
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    def reverse_number(n):
        return int(str(n)[::-1])

    n = input_and_validate()
    print(f"{n} in binary is {bin(n)[2:]}")
    
    # Re-enter the number for sum of digits and reverse number
    n_reentered = int(input("Re-enter the number (without validation): "))
    print(f"Sum of all digits of {n_reentered} is {sum_of_digits(n_reentered)}")
    print(f"Reverse of {n_reentered} is {reverse_number(n_reentered)}")

q3_program()
