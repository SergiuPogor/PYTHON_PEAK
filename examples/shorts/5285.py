# Practical use of int() in various scenarios

# Example: Converting string inputs to integers

input_strings = ["10", "20", "30"]
integers = list(map(int, input_strings))
total = sum(integers)
print(f"Total sum: {total}")

# Example: Handling float to int conversion

float_values = [1.99, 2.75, 3.14]
integer_values = list(map(int, float_values))
print(f"Integer values: {integer_values}")

# Example: Converting hexadecimal string to integer

hex_string = "1A"
decimal_value = int(hex_string, 16)
print(f"Decimal value of hex {hex_string}: {decimal_value}")

# Example: Handling conversion errors

data = ["100", "abc", "200"]
cleaned_data = []

for item in data:
    try:
        cleaned_data.append(int(item))
    except ValueError:
        print(f"Cannot convert '{item}' to integer.")

print(f"Cleaned data: {cleaned_data}")