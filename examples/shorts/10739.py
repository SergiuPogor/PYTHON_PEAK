import logging

# Configure logging to display error messages
logging.basicConfig(level=logging.ERROR)

def risky_operation():
    return 1 / 0  # This will raise a ZeroDivisionError

def handle_exceptions():
    try:
        result = risky_operation()
        print(f"Result is {result}")
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero! Error: %s", str(e))
    except Exception as e:
        logging.error("An unexpected error occurred: %s", str(e))
    finally:
        print("Cleanup actions can go here.")

if __name__ == "__main__":
    handle_exceptions()  # Output: ERROR:root:Attempted to divide by zero! Error: division by zero