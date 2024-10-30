# Example data for transposition
data = [
    ('Alice', 24, 'Engineer'),
    ('Bob', 30, 'Designer'),
    ('Charlie', 22, 'Teacher')
]

# Transposing the data using zip
transposed_data = list(zip(*data))

# Displaying transposed data
for row in transposed_data:
    print(row)

# Using transposed data
transposed_dict = {
    'Names': transposed_data[0],
    'Ages': transposed_data[1],
    'Occupations': transposed_data[2]
}

# Displaying as a dictionary
for key, values in transposed_dict.items():
    print(f"{key}: {', '.join(values)}")