# Example using functools.cmp_to_key for custom sorting

from functools import cmp_to_key

# Custom comparison function
def compare_strings(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

# Sample list to sort
data = ["banana", "apple", "orange", "kiwi"]

# Sorting using cmp_to_key
sorted_data = sorted(data, key=cmp_to_key(compare_strings))

print("Sorted Data:", sorted_data)

# Sorting by string length using a custom comparison
def compare_length(a, b):
    return len(a) - len(b)

# Sorting by length
sorted_by_length = sorted(data, key=cmp_to_key(compare_length))

print("Sorted by Length:", sorted_by_length)