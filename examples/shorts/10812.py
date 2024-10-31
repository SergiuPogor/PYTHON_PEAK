from functools import partial

def multiply(x, y):
    return x * y

# Create a new function that doubles the input
double = partial(multiply, 2)

# Example usage
if __name__ == "__main__":
    # Using the partial function
    result = double(5)  # This effectively calls multiply(2, 5)
    print(result)  # Output: 10

    # Another example to add a fixed value
    def add(x, y):
        return x + y

    # Create a new function to add 10
    add_ten = partial(add, 10)

    # Using the new function
    print(add_ten(5))  # Output: 15