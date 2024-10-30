import os
from time import time

# Measure performance between os.listdir and os.scandir
def measure_performance(directory: str):
    # Using os.listdir to iterate
    start_listdir = time()
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)  # Fetch file size for comparison
    listdir_time = time() - start_listdir

    # Using os.scandir to iterate
    start_scandir = time()
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                size = entry.stat().st_size  # Fetch file size directly
    scandir_time = time() - start_scandir

    print(f"os.listdir took {listdir_time:.6f} seconds")
    print(f"os.scandir took {scandir_time:.6f} seconds")

# Example directory path
test_directory = "/tmp/test"

# Create test directory and files for demonstration
def create_test_files(dir_path):
    os.makedirs(dir_path, exist_ok=True)
    for i in range(1, 1001):
        with open(os.path.join(dir_path, f"file_{i}.txt"), "w") as f:
            f.write("This is a test file\n" * 100)

# Custom function to scan directory and process files
def process_files_with_scandir(directory: str):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"File: {entry.name} | Size: {entry.stat().st_size} bytes")
            elif entry.is_dir():
                print(f"Directory: {entry.name}")

# Example usage in a real scenario
if __name__ == "__main__":
    # Create test files
    create_test_files(test_directory)

    # Measure performance
    measure_performance(test_directory)

    # Process files using os.scandir
    print("\nProcessing files with os.scandir:")
    process_files_with_scandir(test_directory)

    # Cleanup after test
    for file_name in os.listdir(test_directory):
        os.remove(os.path.join(test_directory, file_name))
    os.rmdir(test_directory)