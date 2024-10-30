import os
from contextlib import suppress

# Function to safely read files without raising errors
def read_file(filepath):
    with suppress(FileNotFoundError, IsADirectoryError):
        with open(filepath, 'r') as file:
            return file.read()
    # If we reach here, it means the file was not read
    return None

# Example usage of the read_file function
if __name__ == "__main__":
    paths = [
        '/tmp/test/input.txt',  # Assume this file exists
        '/tmp/test/non_existent_file.txt',  # This file does not exist
        '/tmp/test/input.zip'  # This is not a text file
    ]

    for path in paths:
        content = read_file(path)
        if content is None:
            print(f"Could not read file: {path}")
        else:
            print(f"Content of {path}:\n{content}")