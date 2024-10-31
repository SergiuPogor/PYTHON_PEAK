def process_large_file(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)  # Read a chunk of the file
            if not chunk:  # Check if the end of the file is reached
                break
            process_chunk(chunk)  # Process the current chunk

def process_chunk(chunk):
    # Simulating processing of the chunk
    print(f"Processing chunk of size: {len(chunk)} bytes")

# Example usage
if __name__ == "__main__":
    process_large_file('/tmp/test/input.txt', chunk_size=2048)  # Adjust chunk size as needed