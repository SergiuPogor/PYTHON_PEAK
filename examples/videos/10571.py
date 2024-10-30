import os
import contextlib
import tempfile

@contextlib.contextmanager
def temporary_directory():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir  # Provide the temporary directory to the context
    finally:
        # Clean up the temporary directory
        os.rmdir(temp_dir)

def main():
    try:
        with temporary_directory() as temp_dir:
            print(f"Temporary directory created at: {temp_dir}")
            # Use the temporary directory for your operations
            temp_file_path = os.path.join(temp_dir, "temp_file.txt")
            with open(temp_file_path, 'w') as f:
                f.write("This is a temporary file.")
            print(f"Temporary file created at: {temp_file_path}")
            # Perform operations with temp_file here...
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# This code demonstrates how to create a temporary directory 
# using contextlib. It ensures that the directory is cleaned 
# up after use, maintaining a tidy file system.