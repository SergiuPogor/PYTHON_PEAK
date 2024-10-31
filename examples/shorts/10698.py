import os

# Example of creating file paths in a cross-platform manner
# Define base directory
base_dir = os.path.dirname(__file__)  # Current directory

# Constructing file paths using os.path.join
data_file = os.path.join(base_dir, 'data', 'input.txt')
output_file = os.path.join(base_dir, 'output', 'result.txt')

# Check if the directories exist, if not create them
os.makedirs(os.path.dirname(data_file), exist_ok=True)
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Writing some data to the input file
with open(data_file, 'w') as f:
    f.write("Sample data for processing.\n")

# Reading data from the input file
with open(data_file, 'r') as f:
    content = f.read()

# Writing processed data to the output file
with open(output_file, 'w') as f:
    f.write("Processed content:\n")
    f.write(content)

# Output the path of the created files
print(f"Input file created at: {data_file}")
print(f"Output file created at: {output_file}")