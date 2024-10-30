def merge_lists_to_dict(keys, values):
    # Ensure both lists are of the same length
    if len(keys) != len(values):
        raise ValueError("Both lists must be of the same length.")

    # Using zip to pair keys and values
    merged_dict = dict(zip(keys, values))
    return merged_dict

if __name__ == "__main__":
    # Sample lists
    keys = ["name", "age", "city"]
    values = ["Alice", 30, "New York"]

    # Merging lists into a dictionary
    result = merge_lists_to_dict(keys, values)
    print(result)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

    # Another example with different data
    keys2 = ["product", "price", "quantity"]
    values2 = ["Laptop", 999.99, 5]
    
    # Merging another pair of lists
    result2 = merge_lists_to_dict(keys2, values2)
    print(result2)  # Output: {'product': 'Laptop', 'price': 999.99, 'quantity': 5}