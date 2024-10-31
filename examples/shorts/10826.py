# Example of using itertools.product for Cartesian Products

from itertools import product

# Define some sample data
colors = ['red', 'blue', 'green']
sizes = ['S', 'M', 'L']
shapes = ['circle', 'square']

# Generate Cartesian product using itertools.product
combinations = product(colors, sizes, shapes)

# Convert combinations to a list for easy viewing
combinations_list = list(combinations)

# Display the results
for combo in combinations_list:
    print(combo)

# Output will be:
# ('red', 'S', 'circle')
# ('red', 'S', 'square')
# ('red', 'M', 'circle')
# ('red', 'M', 'square')
# ...
# ('green', 'L', 'square')