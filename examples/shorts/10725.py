from contextlib import ExitStack

# Example function to open multiple files safely
def read_multiple_files(file_names):
    with ExitStack() as stack:
        files = [stack.enter_context(open(file_name)) for file_name in file_names]
        contents = [file.read() for file in files]
    return contents

# Sample usage
file_list = ['/tmp/test/input.txt', '/tmp/test/input.zip']
try:
    data = read_multiple_files(file_list)
    for idx, content in enumerate(data):
        print(f"Content of file {file_list[idx]}:\n{content}\n")
except Exception as e:
    print(f"An error occurred: {e}")