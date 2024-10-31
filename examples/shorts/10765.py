import itertools

# Sample data
data = ['apple', 'banana', 'cherry']

# Using itertools to create combinations
combinations = list(itertools.combinations(data, 2))
print("Combinations of 2:", combinations)

# Using itertools to create permutations
permutations = list(itertools.permutations(data, 2))
print("Permutations of 2:", permutations)

# Using itertools to group items
grouped = itertools.groupby(sorted(data, key=lambda x: x[0]))
print("Grouped items:")
for key, group in grouped:
    print(key, list(group))

# Efficiently iterate over a large range with itertools.count
print("Counting from 0 to 10:")
for i in itertools.count(start=0):
    if i > 10:
        break
    print(i)