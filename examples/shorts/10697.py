# Using the with statement for file handling

# This file will be created in the '/tmp/test' directory
file_path = '/tmp/test/sample.txt'

# Writing data to a file using with
with open(file_path, 'w') as file:
    file.write("Hello, this is a test file!\n")
    file.write("Using the with statement ensures it will be closed automatically.")

# Reading data from the file using with
with open(file_path, 'r') as file:
    content = file.readlines()
    
# Output the content read from the file
for line in content:
    print(line.strip())  # Strip to remove extra newlines