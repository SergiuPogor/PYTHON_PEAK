from functools import partial

# A simple function that takes three parameters
def multiply(x, y, z):
    return x * y * z

# Creating a new function that fixes the first argument to 2
double_multiply = partial(multiply, 2)

# Now, we only need to provide the other two arguments
result1 = double_multiply(3, 4)  # 2 * 3 * 4 = 24
result2 = double_multiply(5, 6)  # 2 * 5 * 6 = 60

# Creating another function fixing the last argument to 10
multiply_by_ten = partial(multiply, z=10)

result3 = multiply_by_ten(3, 4)  # 3 * 4 * 10 = 120
result4 = multiply_by_ten(5, 6)  # 5 * 6 * 10 = 300

# Displaying the results
print(result1)  # Output: 24
print(result2)  # Output: 60
print(result3)  # Output: 120
print(result4)  # Output: 300