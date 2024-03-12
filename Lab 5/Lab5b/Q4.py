#Q4
# # Task 1: Write a program to determine which class a given Bus object belongs to.
# Task 2: Determine if School_bus is also an instance of the Vehicle class.

# Given code from the images
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

# Creating an instance of Bus named School_bus
School_bus = Bus("School Volvo", 12, 50)

# Task 1: Determine the class of School_bus
class_of_school_bus = str(School_bus.__class__)

# Task 2: Determine if School_bus is an instance of Vehicle
is_school_bus_instance_of_vehicle = isinstance(School_bus, Vehicle)

# Output for both tasks
print(class_of_school_bus) 
print( is_school_bus_instance_of_vehicle)
