import os

def scan_directory(path):
    # Using os.scandir for efficient directory iteration
    with os.scandir(path) as entries:
        for entry in entries:
            # Check if the entry is a file
            if entry.is_file():
                print(f"File: {entry.name}, Size: {entry.stat().st_size} bytes")
            # Check if the entry is a directory
            elif entry.is_dir():
                print(f"Directory: {entry.name}")

def main():
    directory_path = '/tmp/test'  # Adjust this path as needed
    scan_directory(directory_path)

# Run the main function
main()