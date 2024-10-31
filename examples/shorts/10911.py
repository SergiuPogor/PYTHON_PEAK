class FileHandler:
    def __init__(self, filepath, mode):
        self.filepath = filepath
        self.mode = mode
        self.file = None

    # Enter method for setup
    def __enter__(self):
        print(f"Opening file: {self.filepath}")
        self.file = open(self.filepath, self.mode)
        return self.file

    # Exit method for cleanup
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            print(f"Closing file: {self.filepath}")
            self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")

# Use custom context manager
file_path = '/tmp/test/input.txt'

# Write and read with automatic handling
with FileHandler(file_path, 'w') as f:
    f.write("Hello, context managers!")

with FileHandler(file_path, 'r') as f:
    content = f.read()
    print("Content read:", content)