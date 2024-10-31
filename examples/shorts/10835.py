from collections import Counter

# Sample data: list of items
items = [
    'apple', 'banana', 'orange', 'apple', 
    'banana', 'banana', 'grape', 'orange'
]

# Use Counter to count item frequencies
item_count = Counter(items)

# Display the counts
for item, count in item_count.items():
    print(f'{item}: {count}')

# Check frequency of a specific item
print(f'Frequency of grapes: {item_count["grape"]}')  # Output: Frequency of grapes: 1

# Check frequency of a non-existent item
print(f'Frequency of mango: {item_count["mango"]}')  # Output: Frequency of mango: 0