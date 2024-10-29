# This script demonstrates how to create a custom exception
# hierarchy in Python. It includes a base exception and two
# derived exceptions for specific error scenarios.

class MyBaseException(Exception):
    """Base class for other exceptions."""
    pass

class ValidationError(MyBaseException):
    """Raised when a validation error occurs."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ProcessingError(MyBaseException):
    """Raised when a processing error occurs."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)

def validate_data(data):
    """Validate the input data."""
    if not isinstance(data, dict):
        raise ValidationError("Input data must be a dictionary.")

    if 'name' not in data:
        raise ValidationError("Missing 'name' key in input data.")

def process_data(data):
    """Process the input data."""
    try:
        validate_data(data)
        # Simulating a processing error
        if data['name'] == 'error':
            raise ProcessingError("Processing failed due to invalid name.", 500)
        print("Processing data:", data)
    except MyBaseException as e:
        print(f"Error: {e.message}")

def main():
    # Example inputs
    data_valid = {"name": "John"}
    data_invalid = {"age": 25}
    data_processing_error = {"name": "error"}

    # Valid input
    process_data(data_valid)
    
    # Invalid input
    process_data(data_invalid)
    
    # Processing error
    process_data(data_processing_error)

if __name__ == "__main__":
    main()