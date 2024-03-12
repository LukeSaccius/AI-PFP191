def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Recursive Binary Search
def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        return -1

# Iterative Binary Search
def binary_search_iterative(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

search_key = 25
seq_search_result = sequential_search(sorted_arr, search_key)
if seq_search_result != -1:
    print(f"Found key at position {seq_search_result} in List")
else:
    print("Not Found!")

bin_search_result = binary_search_iterative(sorted_arr, search_key)
if bin_search_result != -1:
    print(f"Found key at position {bin_search_result} in List using Iterative Binary Search")
else:
    print("Not Found using Iterative Binary Search")

bin_search_result_rec = binary_search_recursive(sorted_arr, 0, len(sorted_arr)-1, search_key)
if bin_search_result_rec != -1:
    print(f"Found key at position {bin_search_result_rec} in List using Recursive Binary Search")
else:
    print("Not Found using Recursive Binary Search")

