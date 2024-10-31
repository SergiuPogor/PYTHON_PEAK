# Using 'nonlocal' to Control State Across Nested Functions

def outer_function():
    counter = 0  # Define a counter variable in the outer scope

    def nested_increment(step):
        # Use nonlocal to modify 'counter' from the enclosing function's scope
        nonlocal counter
        counter += step
        return counter

    # Run nested_increment multiple times with different steps
    print(nested_increment(3))  # Output: 3
    print(nested_increment(2))  # Output: 5
    print(nested_increment(10))  # Output: 15

    return counter

# Calling the outer_function to see the final value of 'counter' after nested increments
result = outer_function()
print("Final Counter Value:", result)  # Final Counter Value: 15