import logging
import os

# Configure logging settings
def setup_logging():
    log_file = os.path.join('/tmp/test', 'app.log')
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Sample function to demonstrate logging
def perform_calculation(x, y):
    logging.info("Starting calculation.")
    try:
        result = x / y
        logging.info("Calculation successful: %s", result)
    except ZeroDivisionError:
        logging.error("Division by zero error: x=%s, y=%s", x, y)

def main():
    setup_logging()
    perform_calculation(10, 2)  # Normal operation
    perform_calculation(10, 0)  # Will raise an error

if __name__ == "__main__":
    main()