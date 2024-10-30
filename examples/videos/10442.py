class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        # Open the file and return the file object
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Ensure the file is closed properly
        if self.file:
            self.file.close()
        # Handle exceptions if needed
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return True  # Suppress exception if handled

def main():
    # Using the custom context manager to write to a file
    with FileHandler('output.txt') as file:
        file.write("Hello, World!\n")
        file.write("This is a custom context manager demo.\n")
        # You can perform other operations with the file here

if __name__ == "__main__":
    main()