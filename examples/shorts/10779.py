from itertools import product

# Define two lists to create Cartesian products
list_a = ['red', 'blue', 'green']
list_b = ['circle', 'square']

# Generate Cartesian products using itertools.product
cartesian_product = list(product(list_a, list_b))

# Print the result
print("Cartesian Product of list_a and list_b:")
for item in cartesian_product:
    print(item)

# Defining three lists for more complex combinations
list_c = ['small', 'medium', 'large']

# Generate Cartesian product with three lists
complex_product = list(product(list_a, list_b, list_c))

# Print the complex combinations
print("\nComplex Cartesian Product of list_a, list_b, and list_c:")
for item in complex_product:
    print(item)