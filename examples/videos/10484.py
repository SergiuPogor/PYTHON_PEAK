from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode='r'):
    """Context manager for opening a file safely."""
    try:
        file = open(file_name, mode)
        yield file  # Control is passed to the block inside the with statement
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        file.close()  # Ensure the file is closed after the block

def read_file_contents(file_name):
    """Read and print contents of a file using the context manager."""
    with open_file(file_name) as file:
        contents = file.read()
        print(contents)

def main():
    file_path = '/tmp/test/input.txt'  # Make sure this file exists with content
    read_file_contents(file_path)

# Uncomment to run the main function
# if __name__ == "__main__":
#     main()