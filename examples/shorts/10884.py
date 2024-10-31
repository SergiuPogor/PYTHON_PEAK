import itertools

def generate_combinations(elements, r):
    """Generate combinations of length r from the elements."""
    return list(itertools.combinations(elements, r))

def generate_permutations(elements, r):
    """Generate permutations of length r from the elements."""
    return list(itertools.permutations(elements, r))

def main():
    elements = ['A', 'B', 'C', 'D']
    
    # Generate combinations of length 2
    combinations = generate_combinations(elements, 2)
    print("Combinations (length 2):", combinations)

    # Generate permutations of length 2
    permutations = generate_permutations(elements, 2)
    print("Permutations (length 2):", permutations)

if __name__ == "__main__":
    main()