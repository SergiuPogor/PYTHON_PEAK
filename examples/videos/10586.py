import select
import socket
import sys
import os

# Server setup for non-blocking I/O
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)
server_socket.setblocking(False)

# Tracking connections and messages
inputs = [server_socket]
outputs = []
message_queues = {}

# Main loop
while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    for s in readable:
        if s is server_socket:
            # Handle a new connection
            connection, client_address = s.accept()
            connection.setblocking(False)
            inputs.append(connection)
            message_queues[connection] = []
        else:
            # Handle incoming data
            data = s.recv(1024)
            if data:
                # Queue message for sending
                message_queues[s].append(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                # Close connection if no data received
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_queues[s]

    for s in writable:
        if message_queues[s]:
            next_msg = message_queues[s].pop(0)
            s.send(next_msg)
        else:
            outputs.remove(s)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]

# Client Example - Open, write, close operations on a socket with select
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))
client_socket.setblocking(0)
message = "Hello, server!"

# Sending message in a non-blocking way
while message:
    try:
        sent = client_socket.send(message.encode())
        message = message[sent:]
    except BlockingIOError:
        print("Socket is busy, waiting...")
        select.select([], [client_socket], [])

# Close connection
client_socket.close()