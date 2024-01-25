try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        raise ValueError("Number must be positive.")
    
    # Print the number pattern
    print("\nNumber Pattern:")
    for i in range(1, n + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))

    # Calculate and print the sum using the formula n*(n+1)/2
    print(f"\nSum of numbers from 1 to {n} is: {n * (n + 1) // 2}")
except ValueError as e:
    print(f"Invalid input! {e}")
