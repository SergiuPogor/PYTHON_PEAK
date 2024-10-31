def read_file(file_path):
    # Automatically handle file opening and closing
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def write_to_file(file_path, content):
    # Automatically handle file opening and closing
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    input_file = '/tmp/test/input.txt'
    output_file = '/tmp/test/output.txt'
    
    # Writing some data to a file
    write_to_file(input_file, "Hello, World!\nWelcome to Python file handling!")
    
    # Reading data back from the file
    content = read_file(input_file)
    print("File Content:")
    print(content)

if __name__ == "__main__":
    main()