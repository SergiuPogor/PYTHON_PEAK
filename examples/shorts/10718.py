# Custom exception handling using BaseException for full error coverage
import os
import sys

# Custom error class that inherits from BaseException, allowing coverage of all exceptions
class CriticalFileError(BaseException):
    def __init__(self, message, filename):
        self.message = message
        self.filename = filename
        super().__init__(message)

# A function to check the presence of critical files, raises CriticalFileError on failure
def check_critical_file(filepath):
    if not os.path.isfile(filepath):
        raise CriticalFileError(f"Critical file missing: {filepath}", filepath)
    print(f"File '{filepath}' found successfully.")

try:
    # Simulate check on a critical file
    check_critical_file('/tmp/test/config.ini')
    check_critical_file('/tmp/test/data.csv')
except CriticalFileError as e:
    # Handle missing critical files or other system errors
    print(f"Error: {e.message} - Check file: {e.filename}")
except BaseException as base_error:
    # BaseException block captures any unexpected system-level issues
    print(f"Unexpected error: {base_error}")
    sys.exit(1)

# Additional test to demonstrate flexibility - handling KeyboardInterrupt specifically
try:
    while True:
        pass  # Infinite loop; press Ctrl+C to test interrupt handling
except CriticalFileError:
    print("Critical file error occurred.")
except KeyboardInterrupt:
    print("Process interrupted by user - handled at system level.")