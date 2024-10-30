import os
import zipfile

# Context management for file and resource handling using 'with'
# Ensures that resources like files are properly closed, even if errors occur

# Create a folder and write sample text to multiple files
file_path = '/tmp/test'
os.makedirs(file_path, exist_ok=True)

# Example 1: Handling file reading and writing with 'with' to avoid resource leaks
file_names = ['input1.txt', 'input2.txt', 'input3.txt']
sample_data = ["Hello, this is file 1", "Greetings from file 2", "File 3 is here"]

# Write content to files safely
for i, name in enumerate(file_names):
    with open(os.path.join(file_path, name), 'w') as f:
        f.write(sample_data[i])

# Read from the files in a safe and managed way
for name in file_names:
    with open(os.path.join(file_path, name), 'r') as f:
        print(f.read())

# Example 2: Using 'with' for zip file extraction
zip_file = '/tmp/test/input.zip'
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall('/tmp/test/extracted_files')

# Example 3: Using 'with' for network connections or database management
# Simulating a context manager for database connections
class DatabaseConnection:
    def __enter__(self):
        print("Opening database connection")
        # Code to open connection goes here
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")
        # Code to close connection and cleanup goes here
        if exc_type:
            print(f"An error occurred: {exc_val}")

# Usage of the custom context manager for safe DB connection handling
with DatabaseConnection() as db_conn:
    # Interact with the database
    print("Executing database commands...")

# Example 4: Lock management using threading.Lock() for safe resource access in multithreading
import threading

lock = threading.Lock()

# Simulating thread-safe resource access
def thread_safe_function(thread_id):
    with lock:
        print(f"Thread {thread_id} has the lock")
        # Simulate resource operation that requires the lock

threads = []
for i in range(3):
    t = threading.Thread(target=thread_safe_function, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Example 5: Handle exceptions automatically with 'with'
# Suppose there's an issue while processing the file, 'with' still ensures proper cleanup
try:
    with open(os.path.join(file_path, 'non_existent_file.txt'), 'r') as f:
        print(f.read())
except FileNotFoundError as e:
    print(f"Error: {e}")

# Conclusion: Using 'with' in Python simplifies and secures resource management