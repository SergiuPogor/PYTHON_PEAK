from collections import defaultdict

# Using defaultdict to count occurrences of items
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# Create a defaultdict for counting
count_dict = defaultdict(int)

# Count each item
for item in items:
    count_dict[item] += 1

# Display the counts
for item, count in count_dict.items():
    print(f"{item}: {count}")

# Using defaultdict for grouping data
grouped_data = defaultdict(list)

# Sample data for grouping
data = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'orange')]

# Grouping items by their category
for category, name in data:
    grouped_data[category].append(name)

# Display grouped data
for category, names in grouped_data.items():
    print(f"{category}: {names}")

# This example shows how defaultdict simplifies counting and grouping operations,
# reducing the need for checking if keys exist.