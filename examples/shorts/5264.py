# Convert integers to octal representation using oct() function
def convert_numbers_to_octal(numbers):
    octal_representations = [oct(num) for num in numbers]
    return octal_representations

# Example usage with a list of integers
numbers = [8, 16, 32, 64]
octal_numbers = convert_numbers_to_octal(numbers)

# Print the octal representations
for num, octal in zip(numbers, octal_numbers):
    print(f"Decimal: {num} -> Octal: {octal}")