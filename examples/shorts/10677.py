# Using the `with` statement for resource management with custom context manager
from contextlib import contextmanager
import zipfile

# Custom context manager for handling a resource - a zip file
@contextmanager
def open_zip(file_path, mode='r'):
    zip_file = zipfile.ZipFile(file_path, mode)
    try:
        yield zip_file
    finally:
        zip_file.close()

# Example usage of the `with` statement for managing both file and zip resources
def main():
    # Path to our test input file
    input_path = '/tmp/test/input.txt'
    zip_path = '/tmp/test/input.zip'
    
    # Writing content to a file to demonstrate resource management
    with open(input_path, 'w') as file:
        file.write("This is a test file with resource management in Python.")

    # Using the custom `with` statement to manage the zip file resource
    with open_zip(zip_path, 'w') as zip_file:
        zip_file.write(input_path, arcname="test_resource.txt")
        
    # Reading content back to verify
    with open_zip(zip_path, 'r') as zip_file:
        with zip_file.open("test_resource.txt") as file:
            print(file.read().decode())  # Displaying content for verification

main()