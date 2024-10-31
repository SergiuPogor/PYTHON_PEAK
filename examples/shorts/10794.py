# Advanced use of enumerate() for more efficient looping
data = ["Alice", "Bob", "Charlie", "Diana"]

# Basic loop with enumerate, tracking index and name directly
for index, name in enumerate(data, start=1):
    print(f"{index}: {name}")

# Example: File processing with line numbers
file_path = "/tmp/test/input.txt"
with open(file_path, "r") as file:
    for line_number, line_content in enumerate(file, start=1):
        if "ERROR" in line_content:
            print(f"Error on line {line_number}: {line_content.strip()}")

# Example: Data transformation with index-based logic
values = [10, 15, 20, 25]
updated_values = [value * (index + 1) for index, value in enumerate(values)]
print(updated_values)  # [10, 30, 60, 100]

# Real-world scenario: Processing names with special index logic
names = ["Anna", "Ben", "Cara", "Dave"]
for idx, person in enumerate(names):
    if idx % 2 == 0:
        print(f"Index {idx} is even, processing {person.upper()}...")
    else:
        print(f"Index {idx} is odd, skipping {person}")