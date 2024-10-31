from collections import Counter

# Sample data: a list of items
items = ['apple', 'banana', 'orange', 'apple', 'banana', 'banana']

# Using Counter to count occurrences
item_counts = Counter(items)

# Displaying the count of each item
print(item_counts)  # Outputs: Counter({'banana': 3, 'apple': 2, 'orange': 1})

# Getting the most common elements
most_common = item_counts.most_common(2)
print(most_common)  # Outputs: [('banana', 3), ('apple', 2)]

# Count characters in a string
char_count = Counter('hello world')
print(char_count)  # Outputs: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})