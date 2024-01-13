#Task 1
def tong(n) :
    if n == 1: 
        return 1 
    return n + tong(n-1)
print(tong(10))

#Task 2
def display_student(name, age):
    print(name, age)

display_student('Emma', 26)
# Assigning new name to the function
show_student = display_student

# Now you can call the function using its new name
show_student("Emma", 26)
