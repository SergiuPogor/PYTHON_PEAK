import logging
import socket

# Custom logging handler that sends logs to a network socket
class NetworkLogHandler(logging.Handler):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def emit(self, record):
        log_entry = self.format(record)
        self.socket.sendall(log_entry.encode('utf-8'))

    def close(self):
        self.socket.close()
        super().close()

# Set up the logger
logger = logging.getLogger('customLogger')
logger.setLevel(logging.DEBUG)

# Console handler for logging to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# File handler for logging to a file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.WARNING)

# Network handler for sending logs to a remote server
network_handler = NetworkLogHandler('localhost', 9000)
network_handler.setLevel(logging.ERROR)

# Create a formatter and set it for all handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
network_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(network_handler)

# Sample log messages
logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')

# If you need to run this as a script, ensure to create a simple TCP server to receive logs.