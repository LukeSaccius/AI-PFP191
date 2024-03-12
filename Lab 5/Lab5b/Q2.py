#Q2
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
# Bus class inheriting from Vehicle from Question 1
class Bus(Vehicle):
    # Overriding the seating_capacity method from Task 2
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# Create an instance of Bus for Task 1
school_bus_task1 = Bus("School Volvo", 180, 12)

# Task 1 output string
task1_output = f"Vehicle Name: {school_bus_task1.name} Speed: {school_bus_task1.max_speed} Mileage: {school_bus_task1.mileage}"

# Task 2: Output string for seating capacity (default of 50)
task2_output = school_bus_task1.seating_capacity()

print(task1_output)
print(task2_output)