def int_to_hex(value):
    if isinstance(value, int):
        return hex(value)
    else:
        raise ValueError("Input must be an integer")

# Convert integers to hexadecimal
value1 = 255
value2 = 1234

# Print hexadecimal representation
print(f"Hex of {value1} is {int_to_hex(value1)}")
print(f"Hex of {value2} is {int_to_hex(value2)}")