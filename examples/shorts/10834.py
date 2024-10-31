from collections import defaultdict

# Create a defaultdict for counting item occurrences
item_count = defaultdict(int)

# Sample data: list of items
items = ['apple', 'banana', 'orange', 'apple', 'banana', 'banana']

# Count each item in the list
for item in items:
    item_count[item] += 1

# Display the counts
for item, count in item_count.items():
    print(f'{item}: {count}')

# Accessing a missing key will not raise KeyError
print(f'Grapes count: {item_count["grapes"]}')  # Output: Grapes count: 0