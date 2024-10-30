class DataProcessingError(Exception):
    def __init__(self, message, file_path, user_id, transaction_id=None):
        super().__init__(message)
        self.file_path = file_path
        self.user_id = user_id
        self.transaction_id = transaction_id

    def __str__(self):
        details = f"File: {self.file_path}, User ID: {self.user_id}"
        if self.transaction_id:
            details += f", Transaction ID: {self.transaction_id}"
        return f"{self.args[0]} ({details})"


# Sample function using the custom exception
def process_user_file(file_path, user_id):
    try:
        # Simulate file processing
        if not file_path.startswith('/tmp/test/'):
            raise DataProcessingError(
                "Invalid file path accessed",
                file_path=file_path,
                user_id=user_id
            )

        # Simulating reading data
        with open(file_path, 'r') as file:
            data = file.read()
        
        # Processing logic
        if "ERROR" in data:
            raise DataProcessingError(
                "Error found in file data",
                file_path=file_path,
                user_id=user_id,
                transaction_id=1001  # Example ID for tracking
            )

        print(f"Data processed for user {user_id}")

    except DataProcessingError as e:
        print("DataProcessingError encountered:", e)


# Example Usage
try:
    process_user_file('/tmp/test/input.txt', user_id=42)
    process_user_file('/invalid/path/file.txt', user_id=24)
except DataProcessingError as e:
    # Handle or log the exception with context
    print(f"Critical issue: {e}")