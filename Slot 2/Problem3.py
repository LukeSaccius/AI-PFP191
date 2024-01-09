# Find unique numbers in the array
arr = list(map(int, input("Enter the numbers separated by space: ").split()))

# Find and display unique numbers in the array
unique_nums = set(arr)
print("The unique numbers in the array are:")
for num in unique_nums:
    print(num)
