import shutil
import os

# Path to the directory to delete
directory_path = '/tmp/test/old_data'

# Ensure the directory exists
if os.path.exists(directory_path):
    # Use shutil.rmtree to delete the directory and all its contents
    shutil.rmtree(directory_path)
    print(f'Directory {directory_path} and its contents have been deleted.')
else:
    print(f'Directory {directory_path} does not exist.')