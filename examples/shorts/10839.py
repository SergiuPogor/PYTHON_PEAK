def modify_list(my_list):
    my_list.append(4)  # This modifies the original list

def safe_modify_list(my_list):
    my_list_copy = my_list[:]  # Create a copy of the list
    my_list_copy.append(5)  # Modify the copy, not the original
    return my_list_copy

# Example usage
original_list = [1, 2, 3]
modify_list(original_list)  # This will change original_list
print(original_list)  # Output: [1, 2, 3, 4]

# Using safe_modify_list to avoid modifying the original
new_list = safe_modify_list(original_list)
print(original_list)  # Output: [1, 2, 3, 4]
print(new_list)  # Output: [1, 2, 3, 5]