# Multi-line lambda function example

from functools import reduce

# Define a multi-line lambda for complex calculations
complex_lambda = (
    lambda x: (
        (result := x * 2) + 3,
        (result := result + 5),
        result * 2
    )[-1]  # Return the last value
)

# Using map with the multi-line lambda
numbers = [1, 2, 3, 4]
result_map = list(map(complex_lambda, numbers))

# Using filter to select even results
filtered_result = list(filter(lambda x: x % 2 == 0, result_map))

# Using reduce to accumulate results
final_result = reduce(lambda a, b: a + b, filtered_result)

print("Mapped results:", result_map)
print("Filtered results (even):", filtered_result)
print("Final accumulated result:", final_result)