# This script demonstrates how to flatten nested lists using
# itertools.chain. It includes multiple examples to show the power
# and flexibility of this method in Python.

import itertools

def flatten_list(nested_list):
    # Flatten the list using itertools.chain
    return list(itertools.chain.from_iterable(nested_list))

def main():
    # Sample nested lists
    nested_list_1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    nested_list_2 = [['a', 'b', 'c'], ['d', 'e'], ['f']]
    nested_list_3 = [[], [1, 2, 3], [], [4, 5, 6]]

    # Flattening the nested lists
    print("Flattened List 1:", flatten_list(nested_list_1))
    print("Flattened List 2:", flatten_list(nested_list_2))
    print("Flattened List 3:", flatten_list(nested_list_3))

    # Handling more complex structures
    complex_nested_list = [
        [1, [2, 3], [4, 5]],
        [6, 7],
        [8, [9, [10]]]
    ]
    
    # Flattening complex nested structures requires a recursive approach
    print("\nFlattening complex nested lists:")
    flat_complex = flatten_complex_list(complex_nested_list)
    print("Flattened Complex List:", flat_complex)

def flatten_complex_list(nested):
    # Recursive function to flatten deeply nested lists
    if isinstance(nested, list):
        for item in nested:
            yield from flatten_complex_list(item)
    else:
        yield nested

if __name__ == "__main__":
    main()