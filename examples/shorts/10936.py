class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")

# Using the custom context manager
with FileHandler('output.txt') as f:
    f.write('Hello, World!\n')
    f.write('Writing to a file with context manager.\n')
    # Uncommenting the next line will trigger the exception handling
    # raise Exception("This is an error!")