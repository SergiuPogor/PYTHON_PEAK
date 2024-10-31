# Example: Using defaultdict to simplify data accumulation logic

from collections import defaultdict

# Example 1: Accumulating values into a list using defaultdict
data = [
    ('apple', 1),
    ('banana', 2),
    ('apple', 3),
    ('banana', 1),
    ('orange', 5)
]

# Initialize defaultdict with list as default factory
accumulated_data = defaultdict(list)

# Accumulate values in the list for each fruit
for fruit, value in data:
    accumulated_data[fruit].append(value)

# Display the accumulated results
print("Accumulated fruit values:", dict(accumulated_data))

# Example 2: Counting occurrences of items using defaultdict
items = ['a', 'b', 'a', 'c', 'b', 'a']

# Initialize defaultdict with int as default factory for counting
item_count = defaultdict(int)

# Count occurrences of each item
for item in items:
    item_count[item] += 1

# Display the count of each item
print("Item counts:", dict(item_count))