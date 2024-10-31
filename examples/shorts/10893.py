from collections import namedtuple

# Define a namedtuple called 'Car'
Car = namedtuple('Car', ['make', 'model', 'year'])

# Create instances of Car
car1 = Car(make='Toyota', model='Corolla', year=2020)
car2 = Car(make='Honda', model='Civic', year=2021)

# Accessing fields by name for better readability
print(f"Car 1: {car1.make} {car1.model} ({car1.year})")
print(f"Car 2: {car2.make} {car2.model} ({car2.year})")

# Use namedtuples in a list for better organization
cars = [car1, car2]

# Display all cars with a loop
for car in cars:
    print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")