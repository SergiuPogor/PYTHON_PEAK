from itertools import chain

# Sample data: Multiple lists to be processed
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Chaining multiple iterators into one
combined = chain(list1, list2, list3)

# Processing the combined iterator
for number in combined:
    print(f"Processing number: {number}")

# This approach allows you to handle data from multiple sources
# without complicating your code structure.