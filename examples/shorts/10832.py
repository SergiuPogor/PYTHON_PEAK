class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    @property
    def area(self):
        # Calculate area using the radius
        return 3.14159 * (self._radius ** 2)

    @property
    def radius(self):
        # Only return the radius, do not allow modification
        return self._radius

# Create an instance of Circle
circle = Circle(5)

# Accessing the read-only property
print(f'Circle radius: {circle.radius}')  # Output: Circle radius: 5
print(f'Circle area: {circle.area}')      # Output: Circle area: 78.54

# Attempting to modify the radius will raise an AttributeError
try:
    circle.radius = 10  # This will fail
except AttributeError as e:
    print(e)  # Output: can't set attribute

# The radius can still be accessed, but not changed
print(f'Circle radius remains: {circle.radius}')  # Output: Circle radius remains: 5