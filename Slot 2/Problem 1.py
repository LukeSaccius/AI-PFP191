# Find the closest number to the average
arr = list(map(int, input("Enter the numbers separated by space: ").split()))

# Find the average value among the numbers
avg = sum(arr) / len(arr)
print("The average value is:", avg)

# Find the first number in the array that is closest to the average
min_diff = float('inf')
min_index = -1
for i in range(len(arr)):
    diff = abs(arr[i] - avg)
    if diff < min_diff:
        min_diff = diff
        min_index = i

# Print the number closest to the average
print(f"The number closest to the average is {arr[min_index]} at index {min_index}.")
