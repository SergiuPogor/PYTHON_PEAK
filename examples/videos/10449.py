import itertools

def advanced_iteration_example(data):
    """
    Demonstrates advanced iteration techniques using itertools.
    
    Args:
    - data: List of elements to process.
    """
    # Using itertools to create combinations
    print("Combinations:")
    for combo in itertools.combinations(data, 2):
        print(combo)

    # Using itertools to create permutations
    print("\nPermutations:")
    for perm in itertools.permutations(data):
        print(perm)

    # Using itertools to cycle through a sequence
    print("\nCycling through data:")
    cycled_data = itertools.cycle(data)
    for _ in range(10):  # Limiting to 10 iterations
        print(next(cycled_data))

    # Using itertools to group data
    print("\nGrouped data (every 2 elements):")
    grouped_data = itertools.zip_longest(*[iter(data)] * 2)
    for group in grouped_data:
        print(group)

# Example usage with sample data
sample_data = ['apple', 'banana', 'cherry']
advanced_iteration_example(sample_data)