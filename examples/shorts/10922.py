# Using functools.reduce() to chain operations in Python
from functools import reduce

# Function to multiply elements in a list
def multiply(x, y):
    return x * y

# Function to sum elements in a list
def add(x, y):
    return x + y

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce to multiply all elements
product = reduce(multiply, numbers)
print(f"The product of {numbers} is: {product}")

# Using reduce to sum all elements
total_sum = reduce(add, numbers)
print(f"The sum of {numbers} is: {total_sum}")

# Using reduce with a lambda function for subtraction
subtraction = reduce(lambda x, y: x - y, numbers)
print(f"The result of subtracting {numbers} is: {subtraction}")