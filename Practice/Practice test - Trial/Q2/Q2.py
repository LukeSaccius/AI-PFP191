import random

def guess_number_game():
    low = 1
    high = 100  # Default value for high

    # Try to get a valid range from the user, if not default to 100
    high_input = input("Enter a range for guessed number: ")
    if high_input.isdigit():
        high = int(high_input)
    else:
        print("Invalid range value! Please type an integer number. Defaulting to 100.")

    print("OUTPUT")

    while True:
        # Make sure that the high value is greater than the low value
        if low > high:
            print(f"Well done! The computer guessed your number {low-1} correctly!")
            print("FINISH")
            break

        # If low and high are equal, we've found the number
        if low >= high:
            print(f"Well done! The computer guessed your number {low} correctly!")
            print("FINISH")
            break

        # The computer makes a guess within the range
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high(h), too low(l), or correct(c)?: ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Well done! The computer guessed your number {guess} correctly!")
            print("FINISH")
            break
        else:
            print("I don't understand your input. Please enter 'h', 'l', or 'c'.")

guess_number_game()
