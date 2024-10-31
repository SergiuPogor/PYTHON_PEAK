import contextlib
import os

# Example 1: Suppressing FileNotFoundError for optional files
with contextlib.suppress(FileNotFoundError):
    with open('/tmp/test/nonexistent_file.txt', 'r') as f:
        data = f.read()

# Example 2: Handling KeyError without cluttering code with try-except
settings = {"theme": "dark", "language": "en"}
with contextlib.suppress(KeyError):
    print("Currency:", settings["currency"])

# Example 3: Using contextlib.suppress for multiple types of ignored errors
with contextlib.suppress(FileNotFoundError, KeyError):
    # Attempting to read a non-existent file, KeyError in dict access
    with open('/tmp/test/input.txt', 'r') as f:
        data = f.read()
    config = {"color": "blue"}
    print(config["size"])  # KeyError suppressed

# Example 4: In real applications, suppressing error when file clean-up might fail
temp_dir = '/tmp/test'
with contextlib.suppress(OSError):
    for file in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, file))  # File might not exist