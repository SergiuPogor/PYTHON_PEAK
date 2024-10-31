import logging
import os

# Set up the logging configuration
log_file = '/tmp/test/app.log'
os.makedirs(os.path.dirname(log_file), exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum log level
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),  # Log to a file
        logging.StreamHandler()          # Log to console
    ]
)

# Sample logging messages
logging.debug("This is a debug message.")
logging.info("Information about application state.")
logging.warning("A warning about a potential issue.")
logging.error("An error occurred during execution.")
logging.critical("Critical issue! Immediate action needed.")

# Log application start
logging.info("Application started successfully.")