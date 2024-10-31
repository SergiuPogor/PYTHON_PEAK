from functools import partial

# Original function with multiple parameters
def multiply(a, b):
    return a * b

# Using functools.partial to create a new function with one fixed argument
double = partial(multiply, 2)

# Test cases
def main():
    print(double(5))  # Output: 10
    print(double(10)) # Output: 20

    # Another partial function with different fixed argument
    triple = partial(multiply, 3)
    print(triple(5))  # Output: 15

if __name__ == "__main__":
    main()  # Execute the main function