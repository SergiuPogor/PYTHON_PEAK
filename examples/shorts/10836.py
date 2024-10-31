from contextlib import ExitStack

# Define file names to open
file_names = ['file1.txt', 'file2.txt', 'file3.txt']

# Using ExitStack to manage multiple file contexts
with ExitStack() as stack:
    # Open each file and add its context to the stack
    files = [stack.enter_context(open(file_name, 'r')) for file_name in file_names]
    
    # Read and print the content of each file
    for f in files:
        print(f'Content of {f.name}:')
        print(f.read())

# At this point, all files are automatically closed