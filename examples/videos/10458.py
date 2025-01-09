import os

def filter_files(dir_path, extension):
    # Using os.scandir to iterate through directory entries
    with os.scandir(dir_path) as entries:
        for entry in entries:
            # Check if entry is a file and matches the extension
            if entry.is_file() and entry.name.endswith(extension):
                print(f"Found file: {entry.name} (Size: {entry.stat().st_size} bytes)")

def main():
    directory = '/tmp/test'  # Specify your directory path here
    file_extension = '.txt'   # Change to desired file type
    print(f"Searching for {file_extension} files in {directory}...")
    filter_files(directory, file_extension)

if __name__ == "__main__":
    main()  # Run the main function