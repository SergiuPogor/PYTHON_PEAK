import os


class DirectoryHandler:
    def __init__(self, path):
        self.path = path

    def create_directory(self):
        # Check if the path is a file
        if os.path.isfile(self.path):
            raise NotADirectoryError(f"The path '{self.path}' is a file, not a directory.")

        # Create the directory if it does not exist
        if not os.path.isdir(self.path):
            try:
                os.makedirs(self.path)
            except PermissionError:
                print("PermissionError: You don't have permission to create the directory.")
            except Exception as e:
                print(f"Unexpected error: {e}")


def main():
    # Use a file path as if it were a directory
    directory_path = '/test/new_directory'
    file_path = '/test/new_directory.txt'

    # Create a file with the conflicting name
    try:
        with open(file_path, 'w') as f:
            f.write("This is a file, not a directory.")
    except Exception as e:
        print(f"Unexpected error while creating file: {e}")

    # Initialize DirectoryHandler with a path that is a file
    handler = DirectoryHandler(file_path)

    try:
        handler.create_directory()
    except NotADirectoryError as e:
        print(f"NotADirectoryError: {e}")


if __name__ == "__main__":
    main()


