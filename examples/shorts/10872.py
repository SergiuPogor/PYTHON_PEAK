import tempfile
import os

# Create a named temporary file that can be accessed by other processes
with tempfile.NamedTemporaryFile(delete=False, mode="w+", suffix=".txt") as temp_file:
    # Write to the temp file
    temp_file.write("Temporary content that will be shared.")
    # Obtain the file name for later access
    temp_file_path = temp_file.name
    print(f"Temporary file created at: {temp_file_path}")

# Open and read the temp file in a new process to simulate sharing
with open(temp_file_path, "r") as shared_file:
    content = shared_file.read()
    print("Read from shared temporary file:", content)

# Cleanup: remove the temp file securely
try:
    os.remove(temp_file_path)
    print(f"Temporary file at {temp_file_path} deleted successfully.")
except OSError as e:
    print(f"Error deleting temp file: {e}")