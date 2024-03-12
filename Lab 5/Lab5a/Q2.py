numbers = [1,2,3,4,5,6,7]
numbers2 = [pow(i,2) for i in numbers]
print(numbers2)
list1 = ["Hello", "take"]
list2 = ["Dear", "Sir "]
result = [x + y for x in list1 for y in list2]
print(result)