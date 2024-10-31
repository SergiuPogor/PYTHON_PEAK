# Using pathlib.Path to handle cross-platform file manipulation

from pathlib import Path

# Define a path to a file and directory
file_path = Path("/tmp/test/input.txt")
dir_path = Path("/tmp/test/new_folder")

# Check if the file exists and read its content
if file_path.exists():
    print(f"Reading content from: {file_path}")
    with file_path.open("r") as f:
        content = f.read()
        print("File Content:", content)

# Create a new directory if it doesn't exist
if not dir_path.exists():
    print(f"Creating directory: {dir_path}")
    dir_path.mkdir(parents=True)

# Combine paths for complex structures
log_path = dir_path / "logs" / "app.log"
log_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if needed

# Write to the log file
print(f"Writing to log file at: {log_path}")
with log_path.open("w") as log_file:
    log_file.write("Logging initialized...\n")

# Listing all files in a directory
print("Files in /tmp/test:")
for item in Path("/tmp/test").iterdir():
    if item.is_file():
        print(item.name)