# A simple example of using a generator to stream data
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Yield each line one at a time

def process_data(file_path):
    for line in read_large_file(file_path):
        # Simulate processing each line
        print(f"Processing: {line}")

if __name__ == "__main__":
    process_data('/tmp/test/input.txt')  # Process a large file efficiently