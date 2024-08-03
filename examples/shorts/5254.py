def print_object_id(obj):
    # Print the unique id of the object
    print(f"Object ID: {id(obj)}")

# Create example objects
example_list = [1, 2, 3]
example_string = "Hello, World!"

# Print their unique ids
print_object_id(example_list)
print_object_id(example_string)