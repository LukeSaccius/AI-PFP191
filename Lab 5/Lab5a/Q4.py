# Let's write the Python code for the tasks based on the provided image.

# Task 1: Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
value_20 = tuple1[1][1]  # Accessing the second element of the second list within the tuple
print(value_20)
# Task 2: Unpack the tuple into 4 variables
tuple2 = (10, 20, 30, 40)
a, b, c, d = tuple2  # Unpacking the tuple
print(a)
print(b)
print(c)
print(d)

# Task 3: Swap two tuples in Python
tuple3 = (11, 22)
tuple4 = (99, 88)
tuple3, tuple4 = tuple4, tuple3  # Swapping the tuples

print(tuple3)
print(tuple4)