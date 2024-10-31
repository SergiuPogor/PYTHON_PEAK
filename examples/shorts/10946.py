def outer_function():
    count = 0  # This variable will be shared with inner_function

    def inner_function():
        nonlocal count  # Allows modification of the outer function's variable
        count += 1
        print(f"Count is now: {count}")

    return inner_function  # Return the inner function

# Example usage
counter = outer_function()  # Get the inner function with access to outer state
counter()  # Output: Count is now: 1
counter()  # Output: Count is now: 2
counter()  # Output: Count is now: 3