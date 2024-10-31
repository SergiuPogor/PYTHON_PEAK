# Using itertools.chain to Flatten Nested Iterables
from itertools import chain

# Let's say we have some nested lists representing user inputs
nested_inputs = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eve"],
    ["Frank", "Grace", "Heidi"]
]

# Flatten the nested list using itertools.chain
flattened_inputs = list(chain.from_iterable(nested_inputs))

# Output the flattened list
print("Flattened Inputs:", flattened_inputs)

# Example of flattening a more complex structure
nested_data = [
    (1, 2, 3),
    [4, 5],
    (6, 7, (8, 9)),
    [10, 11]
]

# Flatten the complex structure using recursion and itertools.chain
def flatten(data):
    for item in data:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)  # Recursively flatten
        else:
            yield item

# Flattened version of nested_data
flattened_complex_data = list(flatten(nested_data))

# Output the flattened complex data
print("Flattened Complex Data:", flattened_complex_data)