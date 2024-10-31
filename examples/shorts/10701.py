import contextlib
import os

# Function to safely delete a file
def safe_delete(file_path):
    # Use contextlib.suppress to ignore FileNotFoundError
    with contextlib.suppress(FileNotFoundError):
        os.remove(file_path)

# Example usage
if __name__ == "__main__":
    safe_delete('/tmp/test/non_existent_file.txt')  # This will not raise an error if the file does not exist
    print("Attempted to delete the file without raising errors.")