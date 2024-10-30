def process_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:  # Read line by line
            if line.strip():  # Process non-empty lines
                yield line.strip()  # Yield each line for further processing

if __name__ == "__main__":
    file_path = '/tmp/test/input.txt'
    for processed_line in process_large_file(file_path):
        print(processed_line)  # Print each processed line