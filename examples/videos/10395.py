class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')  # Open the file for writing
        return self.file  # Return the file object

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()  # Close the file
            if exc_type:
                print(f"Error occurred: {exc_value}")  # Handle exceptions if any

def main():
    # Using the custom context manager
    with FileHandler('output.txt') as f:
        for i in range(5):
            f.write(f"This is line {i + 1}\n")  # Writing to the file

if __name__ == "__main__":
    main()