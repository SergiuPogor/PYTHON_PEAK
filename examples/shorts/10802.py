# Code Example: Catching Multiple Exception Types in One Block

def read_file(file_path):
    try:
        # Attempt to read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Content:", content)
    except (FileNotFoundError, PermissionError) as e:
        # Handle specific exceptions together
        print(f"Error: {e}")

# Example file paths
valid_file_path = '/tmp/test/input.txt'  # Assume this file exists and is readable
invalid_file_path = '/tmp/test/missing.txt'  # This file does not exist
protected_file_path = '/tmp/test/protected.txt'  # Assume this file exists but is protected

# Test with valid file
read_file(valid_file_path)

# Test with a missing file
read_file(invalid_file_path)

# Test with a protected file
read_file(protected_file_path)