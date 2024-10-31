import shutil
import os

# Directory path to delete
directory_to_delete = '/tmp/test'

# Example 1: Simple directory tree removal with shutil.rmtree
shutil.rmtree(directory_to_delete)

# Example 2: Directory removal with error handling
def handle_remove_error(func, path, exc_info):
    print(f"Error deleting {path}. Exception: {exc_info}")

# Removing with error handling if any files are protected
try:
    shutil.rmtree(directory_to_delete, onerror=handle_remove_error)
except Exception as e:
    print("Failed to delete directory:", e)

# Example 3: Deleting multiple directories safely
dirs_to_delete = ['/tmp/test', '/tmp/backup']
for dir_path in dirs_to_delete:
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path, onerror=handle_remove_error)

# Example 4: Create, populate, and delete a directory to simulate real usage
os.makedirs(directory_to_delete, exist_ok=True)
with open(f'{directory_to_delete}/file1.txt', 'w') as f:
    f.write('Sample content')
with open(f'{directory_to_delete}/file2.txt', 'w') as f:
    f.write('More content')

# Confirming deletion of populated directories
if os.path.exists(directory_to_delete):
    shutil.rmtree(directory_to_delete)
    print(f"{directory_to_delete} deleted successfully.")