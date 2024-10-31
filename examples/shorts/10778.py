from functools import reduce

# A simple function to multiply two numbers
def multiply(x, y):
    return x * y

# A list of numbers to multiply
numbers = [1, 2, 3, 4, 5]

# Using reduce to multiply all numbers in the list
result = reduce(multiply, numbers)

# Print the result
print("The product of the list is:", result)

# Using reduce with a lambda function for summing
sum_result = reduce(lambda x, y: x + y, numbers)

# Print the sum result
print("The sum of the list is:", sum_result)