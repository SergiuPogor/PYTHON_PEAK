class InvalidInputError(Exception):
    """Custom exception for invalid user inputs."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class DataProcessor:
    def process_data(self, data):
        if not isinstance(data, dict):
            raise InvalidInputError("Data must be a dictionary.")
        if 'name' not in data or 'age' not in data:
            raise InvalidInputError("Data must contain 'name' and 'age'.")

        # Further processing...
        print(f"Processing data for {data['name']}, age: {data['age']}")

def main():
    processor = DataProcessor()

    # Example of valid input
    valid_input = {'name': 'Alice', 'age': 30}
    processor.process_data(valid_input)

    # Example of invalid input
    invalid_input = ['Alice', 30]  # This should raise an exception
    try:
        processor.process_data(invalid_input)
    except InvalidInputError as e:
        print(f"Error: {e}")

    # Another example of invalid input
    incomplete_input = {'name': 'Bob'}  # Missing age
    try:
        processor.process_data(incomplete_input)
    except InvalidInputError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()