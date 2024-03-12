# Task 1: Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
# Create an instance of Vehicle
car = Vehicle(240, 18)

# Display the max_speed and mileage of the created Vehicle instance
car_max_speed = car.max_speed
car_mileage = car.mileage

# Task 2: Vehicle class without any variables and methods
class EmptyVehicle:
    pass

# Show the output for task 1
(car_max_speed, car_mileage)
