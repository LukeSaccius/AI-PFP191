import random

def question3():
    n = random.randint(1, 100)
    while True:
        x = int(input("Guess the number (1-100): "))
        if x == n:
            print("EXACTLY!")
            break
        elif x < n:
            print("n > x")
        else:
            print("n < x")

question3()
