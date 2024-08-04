def process_data(data):
    # Convert list to tuple to ensure immutability
    data_tuple = tuple(data)
    # Perform operations on the tuple
    for item in data_tuple:
        print(item)

# Example usage
data_list = [1, 2, 3, 4, 5]
process_data(data_list)

# Output:
# 1
# 2
# 3
# 4
# 5