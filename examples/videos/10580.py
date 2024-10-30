from pathlib import Path
from zipfile import ZipFile

# Initialize a Path object for the base directory
base_dir = Path("/tmp/test")

# Read from a file using Pathlib (more readable than os.path)
input_file = base_dir / "input.txt"
if input_file.exists():
    # Reading file content as text
    with input_file.open("r") as f:
        content = f.read()
    print("File Content:", content)

# Writing to a new file, automatically handling path creation if needed
output_file = base_dir / "output.txt"
output_file.parent.mkdir(parents=True, exist_ok=True)  # ensures directory exists

with output_file.open("w") as f:
    f.write("This is a sample output using Pathlib!")

# Pathlib makes it easy to zip multiple files by handling paths directly
with ZipFile(base_dir / "output.zip", "w") as zipf:
    for file_path in base_dir.iterdir():
        # Only add .txt files to the zip
        if file_path.suffix == ".txt":
            zipf.write(file_path, arcname=file_path.name)
            print(f"Added {file_path.name} to zip")

# List all .txt files in the directory
txt_files = list(base_dir.glob("*.txt"))
print("Text files in directory:", txt_files)

# Cleaning up by removing all .txt files using Pathlib
for file_path in txt_files:
    file_path.unlink()  # Deletes the file
    print(f"Deleted {file_path.name}")

# Demonstrates moving a file with Pathlib
moved_file = base_dir / "moved_output.txt"
output_file.replace(moved_file)
print(f"Moved file to {moved_file}")