# Efficient use of itertools for combinatorial logic

from itertools import combinations, permutations, product

# Generate combinations of a list
def get_combinations(data, r):
    return list(combinations(data, r))

# Generate permutations of a list
def get_permutations(data):
    return list(permutations(data))

# Generate Cartesian product of two lists
def get_cartesian_product(list1, list2):
    return list(product(list1, list2))

# Sample data
data_list = [1, 2, 3, 4]

# Get combinations of 2 from the data list
combs = get_combinations(data_list, 2)
print("Combinations (2):", combs)

# Get permutations of the data list
perms = get_permutations(data_list)
print("Permutations:", perms)

# Get Cartesian product of two lists
list_a = [1, 2]
list_b = ['a', 'b']
cartesian_prod = get_cartesian_product(list_a, list_b)
print("Cartesian Product:", cartesian_prod)