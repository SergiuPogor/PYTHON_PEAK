import os

# Generator function to read a large file line by line
def read_large_file(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Process the large file with generator
def process_file_in_chunks(file_path: str):
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Use the generator to process each line
    for line in read_large_file(file_path):
        print(f"Processing line: {line}")
        # Simulate some data processing on each line
        if "error" in line:
            print(f"Found error: {line}")
        else:
            print(f"Line is OK: {line}")

# Example use-case: reading a massive log file line by line
def main():
    # Path to a large log file (could be gigabytes in size)
    large_file = '/tmp/test/input.txt'
    
    # Call the processing function
    process_file_in_chunks(large_file)

# Call main function
if __name__ == "__main__":
    main()

# Example content of '/tmp/test/input.txt':
# User logged in
# Data processed
# error: failed to fetch data
# User logged out
# error: connection timeout