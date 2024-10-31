# Efficiently reverse a string in Python using slicing

def reverse_string(s: str) -> str:
    # Return the reversed string using slicing
    return s[::-1]

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)

print("Original String:", input_string)  # Output: Hello, World!
print("Reversed String:", reversed_string)  # Output: !dlroW ,olleH

# Demonstrating with a list of strings
strings = ["Python", "is", "awesome"]
reversed_strings = [reverse_string(s) for s in strings]

print("Reversed List of Strings:", reversed_strings)  # Output: ['nohtyP', 'si', 'emosewa']