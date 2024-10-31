def modify_list(original_list):
    # Attempting to change the original list directly
    original_list.append(4)

def safe_modify(original_list):
    # Create a copy of the original list to avoid side effects
    copied_list = original_list.copy()  # or use copied_list = original_list[:]
    copied_list.append(4)  # Modify the copied list only
    return copied_list

# Example usage
my_list = [1, 2, 3]

# Modifying without safety
modify_list(my_list)
print("After modify_list:", my_list)  # Original list is changed

# Modifying safely
new_list = safe_modify(my_list)
print("After safe_modify:", new_list)  # New list contains the change
print("Original list remains:", my_list)  # Original list is unchanged