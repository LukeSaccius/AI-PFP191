def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return True
        left_sum += num
    return False

def question2():
    arr = list(map(int, input("Enter array elements separated by spaces: ").split()))
    if find_equilibrium_index(arr):
        print("YES")
    else:
        print("NO")

question2()
