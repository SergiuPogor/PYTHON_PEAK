# Example of flattening nested lists using itertools.chain
from itertools import chain

def flatten(nested_list):
    # Using itertools.chain to flatten the nested list
    return list(chain.from_iterable(nested_list))

# Example usage
if __name__ == "__main__":
    # A complex nested list
    nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    
    # Flatten the nested list
    flat_list = flatten(nested)
    print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Another example with different data types
    mixed_nested = [['a', 'b'], [1, 2], [[3, 4], 5]]
    flat_mixed = flatten(mixed_nested)
    print(flat_mixed)  # Output: ['a', 'b', 1, 2, [3, 4], 5]