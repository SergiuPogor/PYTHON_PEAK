# Code Example: Using List Comprehensions for Efficient Data Processing

# Sample data: a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension to create a new list with squares of even numbers
squares_of_evens = [n**2 for n in numbers if n % 2 == 0]

# Output the result
print(f"Squares of even numbers: {squares_of_evens}")

# Another example: Create a list of tuples (number, square)
number_square_pairs = [(n, n**2) for n in numbers]

# Output the pairs
print(f"Number and their squares: {number_square_pairs}")