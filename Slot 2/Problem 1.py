def find_closest_to_average(arr):
    avg = sum(arr) / len(arr)
    closest = min(arr, key=lambda x: (abs(x - avg), x))
    return closest, arr.index(closest), avg

# Example usage with input validation:
while True:
    try:
        numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
        closest_number, closest_index, average = find_closest_to_average(numbers)
        print(f"Average of the array: {average}")
        print(f"Element closest to the average: {closest_number} at index {closest_index}")
        break
    except ValueError:
        print("Please enter only numbers separated by spaces.")
