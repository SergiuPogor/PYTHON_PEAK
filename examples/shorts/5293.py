# Example of using set() for complex data filtering and operations

def filter_unique_elements(data):
    # Create a set to remove duplicates and filter data
    unique_data = set(data)
    
    # Example of set operations
    subset = {1, 2, 3}
    intersection = unique_data.intersection(subset)
    difference = unique_data.difference(subset)
    
    return unique_data, intersection, difference

# Example usage
data_list = [1, 2, 2, 3, 4, 4, 5]
unique, intersect, diff = filter_unique_elements(data_list)

print("Unique elements:", unique)         # Output: Unique elements: {1, 2, 3, 4, 5}
print("Intersection:", intersect)        # Output: Intersection: {1, 2, 3}
print("Difference:", diff)                # Output: Difference: {4, 5}