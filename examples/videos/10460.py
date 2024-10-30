import os
import tempfile
from contextlib import contextmanager

# Custom context manager to handle temporary files with automatic cleanup
@contextmanager
def managed_temp_file(suffix='', prefix='tmp', dir=None):
    # Create a temporary file, return its path, and ensure it's cleaned up
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix, prefix=prefix, dir=dir)
    try:
        yield temp_file.name  # Provide access to the file name only
    finally:
        try:
            os.remove(temp_file.name)  # Ensure file deletion
        except FileNotFoundError:
            pass  # File already deleted; no further action needed

# Example usage in a real-life scenario: handling temporary user data
def process_user_upload(data):
    with managed_temp_file(suffix=".txt", prefix="upload_", dir="/tmp/test") as temp_path:
        with open(temp_path, 'w') as f:
            f.write(data)  # Simulate saving user-uploaded data temporarily

        # Process the file (could involve parsing, validating, etc.)
        print(f"Processing file: {temp_path}")
        
        # File will be automatically deleted upon exit of the context

# Simulate user data handling with a temporary file
user_data = "Sensitive user data that needs processing..."
process_user_upload(user_data)

# Example with temporary files for multiple steps
def multi_step_temp_file_processing():
    # First step: Create and process initial file
    with managed_temp_file(suffix=".log", prefix="step1_", dir="/tmp/test") as step1_path:
        with open(step1_path, 'w') as f:
            f.write("Log data for step 1")  # Write initial data
        print(f"Step 1 processing: {step1_path}")

    # Second step: Generate output based on step 1
    with managed_temp_file(suffix=".log", prefix="step2_", dir="/tmp/test") as step2_path:
        with open(step2_path, 'w') as f:
            f.write(f"Derived from {step1_path}")  # Reference previous file for next process
        print(f"Step 2 processing: {step2_path}")

multi_step_temp_file_processing()

# Example with temporary file in a data pipeline
def temp_file_pipeline(data_chunks):
    temp_files = []
    try:
        # Simulate pipeline where each chunk is processed and temporarily stored
        for i, chunk in enumerate(data_chunks):
            with managed_temp_file(suffix=".txt", prefix=f"chunk_{i}_", dir="/tmp/test") as temp_path:
                with open(temp_path, 'w') as f:
                    f.write(chunk)  # Store each chunk temporarily
                temp_files.append(temp_path)  # Track files for the pipeline
                print(f"Chunk {i} processed and saved at {temp_path}")
    finally:
        # Cleanup handled by the context manager, no need to manually delete
        print("All temporary files handled within context and auto-deleted after processing")

# Simulate a list of data chunks being processed in a pipeline
data_chunks = ["Chunk 1 data...", "Chunk 2 data...", "Chunk 3 data..."]
temp_file_pipeline(data_chunks)