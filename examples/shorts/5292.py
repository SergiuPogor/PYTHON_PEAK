# Example of using reversed() to iterate over a list in reverse order

def print_reversed_list(data):
    # Use reversed() to get an iterator for the reversed list
    for item in reversed(data):
        print(item)

# Example usage
my_list = [1, 2, 3, 4, 5]
print_reversed_list(my_list)  # Output: 5 4 3 2 1