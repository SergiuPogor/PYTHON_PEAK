import csv

# Read data from a CSV file and convert it into a list of dictionaries
def read_csv_to_dict(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        # Use DictReader to read rows as dictionaries
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]  # List comprehension to create a list of dictionaries
    return data

# Example usage
file_path = '/tmp/test/input.txt'  # Ensure this file exists and is properly formatted
csv_data = read_csv_to_dict(file_path)

# Display the content of the CSV as dictionaries
for record in csv_data:
    print(record)

# Handling missing values in CSV
for record in csv_data:
    age = record.get('age', 'Not Specified')  # Get age with a default if missing
    print(f"Name: {record['name']}, Age: {age}")