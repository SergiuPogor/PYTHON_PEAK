import itertools

# Function to generate combinations of a list
def generate_combinations(data, r):
    # Generate all combinations of length r from data
    return list(itertools.combinations(data, r))

# Function to generate permutations of a list
def generate_permutations(data, r):
    # Generate all permutations of length r from data
    return list(itertools.permutations(data, r))

# Sample data
data = ['a', 'b', 'c', 'd']

# Generate combinations of length 2
combinations_result = generate_combinations(data, 2)

# Generate permutations of length 3
permutations_result = generate_permutations(data, 3)

# Display combinations and permutations
print("Combinations of length 2:")
for combo in combinations_result:
    print(combo)

print("\nPermutations of length 3:")
for perm in permutations_result:
    print(perm)

# Save results to files
with open('/tmp/test/combinations.txt', 'w') as combo_file:
    for combo in combinations_result:
        combo_file.write(', '.join(combo) + '\n')

with open('/tmp/test/permutations.txt', 'w') as perm_file:
    for perm in permutations_result:
        perm_file.write(', '.join(perm) + '\n')