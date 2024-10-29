def read_file(file_path):
    # Using with open to read a file
    with open(file_path, 'r') as file:
        content = file.read()  # Read the entire file content
    return content

def write_file(file_path, data):
    # Using with open to write to a file
    with open(file_path, 'w') as file:
        file.write(data)  # Write data to the file

def append_to_file(file_path, data):
    # Using with open to append data to a file
    with open(file_path, 'a') as file:
        file.write(data)  # Append data to the file

# Example usage:
file_to_read = '/tmp/test/input.txt'
file_to_write = '/tmp/test/output.txt'

# Writing some initial data to the output file
write_file(file_to_write, "Hello, World!\n")
append_to_file(file_to_write, "Appending this line.\n")

# Reading the content of the input file
try:
    content = read_file(file_to_read)
    print("File Content:")
    print(content)
except FileNotFoundError:
    print(f"The file {file_to_read} does not exist.")