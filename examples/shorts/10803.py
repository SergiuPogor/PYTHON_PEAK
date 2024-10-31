# Code Example: Using itertools.product for Cartesian Products

import itertools

def generate_combinations(lists):
    try:
        # Generate Cartesian product of input lists
        combinations = list(itertools.product(*lists))
        
        # Display the result
        for combo in combinations:
            print(combo)
    except Exception as e:
        print(f"Error occurred: {e}")

# Example lists
colors = ['red', 'blue']
sizes = ['small', 'medium', 'large']
styles = ['casual', 'formal']

# Create a list of lists for combinations
input_lists = [colors, sizes, styles]

# Generate combinations
generate_combinations(input_lists)