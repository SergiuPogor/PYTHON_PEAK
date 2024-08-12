import os

class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_file(self):
        try:
            with open(self.filepath, 'r') as file:
                return file.read()
        except PermissionError as e:
            print(f"PermissionError: {e}")
            # Handle or log the error appropriately
            return None

    def write_file(self, content):
        try:
            with open(self.filepath, 'w') as file:
                file.write(content)
        except PermissionError as e:
            print(f"PermissionError: {e}")
            # Handle or log the error appropriately

def main():
    # Example usage
    handler = FileHandler('/tmp/test/input.txt')
    content = handler.read_file()
    if content:
        print("File content read successfully.")
    handler.write_file('New content for the file.')

if __name__ == "__main__":
    main()
