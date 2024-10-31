# Using the map function for data transformation

# Sample function to square numbers
def square(x):
    return x ** 2

# Sample data
numbers = [1, 2, 3, 4, 5]

# Applying the square function to all items in the list
squared_numbers = map(square, numbers)

# Converting the map object to a list to see the results
squared_list = list(squared_numbers)

print(squared_list)  # Output: [1, 4, 9, 16, 25]

# Using lambda with map for concise code
squared_lambda = list(map(lambda x: x ** 2, numbers))
print(squared_lambda)  # Output: [1, 4, 9, 16, 25]