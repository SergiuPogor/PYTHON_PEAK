from collections import defaultdict

# Sample application of defaultdict in a real-world case
# Counting items across multiple categories

# 1. defaultdict to count occurrences across categories
category_counts = defaultdict(int)
products = [("Electronics", "TV"), ("Furniture", "Sofa"), ("Electronics", "Laptop"),
            ("Furniture", "Chair"), ("Electronics", "TV")]

# Tally product occurrences without checking if the key exists
for category, item in products:
    category_counts[item] += 1

print(dict(category_counts))

# 2. defaultdict to group lists of items by category
products_by_category = defaultdict(list)

for category, item in products:
    products_by_category[category].append(item)

print(dict(products_by_category))

# 3. Nested defaultdict to create multi-level structures without key errors
user_data = defaultdict(lambda: defaultdict(int))
user_data['user_1']['login_count'] += 1
user_data['user_2']['purchase_count'] += 2

print(dict(user_data))