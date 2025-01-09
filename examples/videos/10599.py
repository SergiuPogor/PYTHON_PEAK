def modify_list(original_list):
    # Modifying the original list directly
    original_list.append(4)
    print(f"Inside function, modified list: {original_list}")

def safe_modify_list(original_list):
    # Creating a copy of the list to avoid modifying the original
    copied_list = original_list.copy()  # or list(original_list) for shallow copy
    copied_list.append(5)
    print(f"Inside function, copied list: {copied_list}")

# Original list
my_list = [1, 2, 3]

# Calling the function that modifies the original list
modify_list(my_list)
print(f"After modify_list call, original list: {my_list}")

# Resetting the original list
my_list = [1, 2, 3]

# Calling the function that modifies a copy
safe_modify_list(my_list)
print(f"After safe_modify_list call, original list: {my_list}")