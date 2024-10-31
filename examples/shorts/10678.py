# Efficient combinatorial logic with Python's itertools module

from itertools import combinations, permutations, product, chain

# Players available for team creation
players = ["Alice", "Bob", "Charlie", "Dana"]

# Generating all unique 2-player combinations
team_combinations = combinations(players, 2)
print("Unique 2-player teams:")
for team in team_combinations:
    print(team)

# Generating all possible orders of players (permutations)
team_permutations = permutations(players, 2)
print("\nAll possible 2-player arrangements:")
for arrangement in team_permutations:
    print(arrangement)

# Generating all possible product combinations of two lists (useful for tournament pairing)
team_a = ["Eve", "Frank"]
team_b = ["George", "Hannah"]
matches = product(team_a, team_b)
print("\nPossible match-ups between Team A and Team B:")
for match in matches:
    print(match)

# Advanced: Chain multiple iterables to process seamlessly
sequences = [range(3), range(5, 8), range(10, 12)]
print("\nCombined sequences from multiple ranges:")
for item in chain(*sequences):
    print(item)