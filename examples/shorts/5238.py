# A real-world example of using ascii() in a Python application

# Function to save string data to a file with ASCII-only characters
def save_ascii_only_string(data, file_path):
    with open(file_path, 'w', encoding='ascii', errors='backslashreplace') as file:
        file.write(ascii(data))

# Sample data with non-ASCII characters
data = "Hello, world! 👋 Привет, мир! こんにちは、世界！"

# File path to save the ASCII-only representation
file_path = '/tmp/test/output.txt'

# Save the ASCII-only string to the file
save_ascii_only_string(data, file_path)

# Read and print the saved ASCII-only string
with open(file_path, 'r', encoding='ascii') as file:
    print(file.read())


