import numpy as np

# Using numpy's arange() for non-integer step values

def generate_sequence(start, stop, step):
    return np.arange(start, stop, step)

# Example usage
sequence = generate_sequence(0, 5, 0.5)
print(sequence)  # Output: [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]