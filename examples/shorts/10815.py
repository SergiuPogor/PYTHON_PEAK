from pathlib import Path

# Create a Path object
base_path = Path('/tmp/test')

# Check if directory exists, create if it doesn't
if not base_path.exists():
    base_path.mkdir(parents=True)

# List all files in the directory
for file in base_path.iterdir():
    if file.is_file():  # Check if it's a file
        print(f"File found: {file.name}")

# Example of reading a text file
input_file = base_path / 'input.txt'
if input_file.exists():
    with input_file.open('r') as f:
        content = f.read()
        print(content)

# Example of writing to a text file
output_file = base_path / 'output.txt'
with output_file.open('w') as f:
    f.write("This is a test output file.")
    print(f"Written to: {output_file.name}")

# Clean up: remove the output file if it exists
if output_file.exists():
    output_file.unlink()
    print(f"Removed: {output_file.name}")