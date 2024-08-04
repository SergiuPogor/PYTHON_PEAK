# Example of using slice() for advanced data manipulation

def advanced_slicing(data):
    # Extract elements from index 1 to 5
    subset = data[1:6]
    
    # Reverse the list using slicing
    reversed_data = data[::-1]
    
    # Skip every second element
    skipped_data = data[::2]
    
    return subset, reversed_data, skipped_data

# Example usage
data_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
subset, reversed_data, skipped_data = advanced_slicing(data_list)

print("Subset:", subset)          # Output: Subset: [20, 30, 40, 50, 60]
print("Reversed:", reversed_data) # Output: Reversed: [90, 80, 70, 60, 50, 40, 30, 20, 10]
print("Skipped:", skipped_data)   # Output: Skipped: [10, 30, 50, 70, 90]