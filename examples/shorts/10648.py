from itertools import zip_longest

# Example lists with different lengths
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92]

# Pairing with zip (shortest list wins)
paired = list(zip(names, scores))
print("Using zip:", paired)

# Pairing with zip_longest to handle different lengths
paired_longest = list(zip_longest(names, scores, fillvalue='N/A'))
print("Using zip_longest:", paired_longest)

# Example of using the result in a dictionary
score_dict = {name: score for name, score in paired_longest}
print("Scores Dictionary:", score_dict)

# Use case: Processing uneven data in a report
report = [f"{name}: {score}" for name, score in paired_longest]
print("Report:", report)