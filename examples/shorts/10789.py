# Using with statement for file handling

# Writing to a file using the with statement
with open('/tmp/test/output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('Using with statement for resource management.\n')

# Reading from a file using the with statement
with open('/tmp/test/output.txt', 'r') as file:
    content = file.readlines()

# Displaying the content of the file
for line in content:
    print(line.strip())

# Using with statement for handling network connections
import socket

# Using with statement for a socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('example.com', 80))
    s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    response = s.recv(4096)

print(response.decode())