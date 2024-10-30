def outer_function():
    count = 0  # Initialize a variable in the outer function
    
    def inner_function():
        nonlocal count  # Declare count as nonlocal to modify it
        count += 1  # Increment count
        return count
    
    return inner_function  # Return the inner function

if __name__ == "__main__":
    my_counter = outer_function()  # Create a counter
    print(my_counter())  # Output: 1
    print(my_counter())  # Output: 2
    print(my_counter())  # Output: 3