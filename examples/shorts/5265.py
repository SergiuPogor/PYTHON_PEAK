import os

def read_file_with_custom_buffer(file_path, buffer_size):
    # Open the file with a custom buffer size
    with open(file_path, 'rb') as file:
        while chunk := file.read(buffer_size):
            # Process each chunk of data
            process_chunk(chunk)

def process_chunk(chunk):
    # Dummy processing function
    # In real use, replace this with actual data processing logic
    print(f"Processing {len(chunk)} bytes")

def write_file_with_custom_buffer(file_path, data, buffer_size):
    # Write data to a file with a custom buffer size
    with open(file_path, 'wb') as file:
        for i in range(0, len(data), buffer_size):
            chunk = data[i:i + buffer_size]
            file.write(chunk)

# Example usage
input_path = '/tmp/test/input.txt'
output_path = '/tmp/test/output.txt'
buffer_size = 8192  # 8 KB buffer size

# Read file using a custom buffer size
read_file_with_custom_buffer(input_path, buffer_size)

# Write data to file using a custom buffer size
data_to_write = b'Some large data...' * 1000  # Example data
write_file_with_custom_buffer(output_path, data_to_write, buffer_size)
