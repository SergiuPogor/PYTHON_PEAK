# Using lambda functions in Python for cleaner code

# Sample data: list of names
names = ['Alice', 'Bob', 'Charlie', 'David']

# Sort names by their length using lambda
sorted_by_length = sorted(names, key=lambda name: len(name))
print("Names sorted by length:", sorted_by_length)

# Filter even numbers from a list using lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Calculate squares of numbers using lambda
squares = list(map(lambda x: x ** 2, numbers))
print("Squares of numbers:", squares)

# Using lambda with reduce to sum numbers
from functools import reduce
total_sum = reduce(lambda a, b: a + b, numbers)
print("Total sum of numbers:", total_sum)