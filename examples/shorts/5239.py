# Example of using bin() in a Python application

def print_binary_representation(numbers):
    binary_representations = {num: bin(num) for num in numbers}
    for num, binary in binary_representations.items():
        print(f"{num}: {binary}")

# Sample data
numbers = [5, 32, 255, 1023, 2048]

# Print binary representation of each number
print_binary_representation(numbers)

# Demonstrating binary arithmetic
def binary_addition(a, b):
    return bin(a + b)

a = 25
b = 37

# Print the result of binary addition
print(f"Binary addition of {a} and {b} is: {binary_addition(a, b)}")





