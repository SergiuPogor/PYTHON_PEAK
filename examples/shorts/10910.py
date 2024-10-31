from pathlib import Path

# Directory path and file example paths
root_dir = Path('/tmp/test')
file_path = root_dir / 'input.txt'
zip_path = root_dir / 'input.zip'

# Create directory and a file if they don't exist
root_dir.mkdir(parents=True, exist_ok=True)
file_path.touch(exist_ok=True)

# Check if the path is a file or directory and handle conditionally
if file_path.is_file():
    print(f"{file_path} is a file")
elif file_path.is_dir():
    print(f"{file_path} is a directory")

# Check if the ZIP file exists, create if missing, and perform operations
if zip_path.exists():
    print(f"{zip_path} already exists.")
else:
    zip_path.touch()
    print(f"{zip_path} created successfully.")

# List all files in the directory and filter only .txt files
txt_files = list(root_dir.glob("*.txt"))
print("Text files in the directory:", txt_files)

# Read and print content if file exists and has content
if file_path.stat().st_size > 0:
    content = file_path.read_text()
    print("File content:", content)
else:
    # Write initial data to file for demo purposes
    file_path.write_text("Hello from pathlib!")
    print("File was empty. Added initial content.")