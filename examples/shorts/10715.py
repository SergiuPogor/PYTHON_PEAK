import logging
import os

# Define log directory and file path
log_dir = "/tmp/test/logs"
log_file = os.path.join(log_dir, "app.log")

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure the logging setup with advanced settings
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",  # Custom format
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Example logging in action
logging.debug("Debugging details: process initialized.")
logging.info("User logged in.")
logging.warning("Warning: API rate limit nearing threshold.")
logging.error("Error occurred while processing input.")
logging.critical("Critical issue! Application shutting down.")

# Demonstrate reading back from log file for validation or troubleshooting
with open(log_file, 'r') as file:
    for line in file:
        print(line.strip())