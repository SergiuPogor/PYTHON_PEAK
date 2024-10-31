# Using map and filter to process data in Python

# Sample data: a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Using filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Displaying results
print("Squared Numbers:", squared_numbers)
print("Even Numbers:", even_numbers)

# In this example, map applies a function to each number,
# while filter selects numbers based on a condition.