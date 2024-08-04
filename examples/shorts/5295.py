# Example demonstrating the use of staticmethod()

class MathUtilities:
    @staticmethod
    def add(x, y):
        # Adds two numbers and returns the result
        return x + y

    @staticmethod
    def multiply(x, y):
        # Multiplies two numbers and returns the result
        return x * y

# Usage example
result_add = MathUtilities.add(5, 3)
result_multiply = MathUtilities.multiply(4, 6)

print("Addition Result:", result_add)        # Output: Addition Result: 8
print("Multiplication Result:", result_multiply) # Output: Multiplication Result: 24