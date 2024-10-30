import csv

# Function to read CSV file using DictReader
def read_csv_as_dict(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        # Create a DictReader object
        reader = csv.DictReader(csvfile)

        # Process each row in the CSV file
        for row in reader:
            # Example: Accessing specific column data
            name = row.get('Name', 'N/A')  # Default to 'N/A' if key is missing
            age = row.get('Age', 'N/A')
            email = row.get('Email', 'N/A')

            # Print out the values
            print(f'Name: {name}, Age: {age}, Email: {email}')

# Example usage
if __name__ == "__main__":
    read_csv_as_dict('/tmp/test/input.txt')