def read_files(file_list):
    return [line.strip() for filename in file_list
            for line in open(filename) if line.strip()]

if __name__ == "__main__":
    files = ['/tmp/test/input.txt', '/tmp/test/input.zip']
    file_contents = read_files(files)  # Get file contents
    print(file_contents)  # Print non-empty lines from files