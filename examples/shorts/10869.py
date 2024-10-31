def create_frozenset_keyed_dict():
    # Create a dictionary with frozensets as keys
    my_dict = {
        frozenset([1, 2, 3]): "Group A",
        frozenset([4, 5, 6]): "Group B",
        frozenset([7, 8, 9]): "Group C"
    }
    
    return my_dict

def check_membership(key):
    # Check if the frozenset key exists in the dictionary
    frozenset_key = frozenset(key)
    my_dict = create_frozenset_keyed_dict()
    
    if frozenset_key in my_dict:
        return f"Key found: {my_dict[frozenset_key]}"
    else:
        return "Key not found."

if __name__ == "__main__":
    result = check_membership([4, 5, 6])  # Check for Group B
    print(result)