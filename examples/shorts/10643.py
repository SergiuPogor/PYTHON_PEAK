from pathlib import Path

# Create a Path object for a given file
file_path = Path("tmp/test/input.txt")

# Check if the file exists
if file_path.exists():
    print("File exists:", file_path)
else:
    print("File does not exist, creating file...")
    file_path.touch()  # Create the file if it doesn't exist

# Read content from the file
with file_path.open('r') as file:
    content = file.read()
    print("File content:", content)

# Create a directory structure if it doesn't exist
new_dir = Path("tmp/test/new_folder")
new_dir.mkdir(parents=True, exist_ok=True)

# Move the file to the new directory
new_file_path = new_dir / file_path.name
file_path.rename(new_file_path)
print("File moved to:", new_file_path)

# List all files in the new directory
print("Files in new directory:")
for item in new_dir.iterdir():
    print(item)