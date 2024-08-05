class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._secret = "This is a secret attribute"

    def start_engine(self):
        print(f"{self.make} {self.model} engine started!")

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Create a Car object
my_car = Car("Tesla", "Model S", 2022)
my_car.display_info()

# Use dir() to inspect the Car object
attributes = dir(my_car)
print("Attributes and methods of my_car:", attributes)

# Use dir() to inspect the Car class itself
class_attributes = dir(Car)
print("Attributes and methods of Car class:", class_attributes)

# Dynamically inspect an imported module
import math
math_attributes = dir(math)
print("Attributes and methods of math module:", math_attributes)

# Check if dir() includes inherited methods
class ElectricCar(Car):
    def charge_battery(self):
        print("Battery charging...")

# Create an ElectricCar object
my_electric_car = ElectricCar("Nissan", "Leaf", 2020)

# Inspect ElectricCar object
electric_car_attributes = dir(my_electric_car)
print("Attributes and methods of my_electric_car:", electric_car_attributes)

