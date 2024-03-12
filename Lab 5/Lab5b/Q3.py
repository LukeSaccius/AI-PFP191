#Q3
# Task 1: Adjust the Vehicle class and create instances of Bus and Car.
class Vehicle:
    color = 'white'  # Class attribute 'color' with a default value 'white'
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        return base_fare + (base_fare * 0.10)  # Including maintenance charge

    # Assuming fare method is a part of the Vehicle class as per the second image provided
    def fare(self):
        base_fare = self.capacity * 100
        return base_fare + (base_fare * 0.10)  # Adding an extra 10% of base fare as maintenance charge

class Car(Vehicle):
    pass

# Task 2: Bus class that calculates fare with an additional maintenance charge.

# Create instances of Bus and Car with specified attributes
school_bus = Bus('School Volvo', 180, 12)
school_bus.capacity = 50  # setting the capacity directly for this instance

# Creating an instance of Car with the name 'Audi Q5', max_speed 240, and mileage 18
family_car = Car('Audi Q5', 240, 18)

# Output for Task 1 
output_task1_bus = f"{Bus.color} {school_bus.name} Speed: {school_bus.max_speed} Mileage: {school_bus.mileage}"
output_task1_car = f"{Car.color} {family_car.name} Speed: {family_car.max_speed} Mileage: {family_car.mileage}"

# Output for Task 2 
# The fare for the Bus is calculated as base fare plus 10% maintenance charge.
output_task2 = f"Total Bus fare is: {school_bus.fare()}"

print(output_task1_bus)
print(output_task1_car)
print( output_task2)    
