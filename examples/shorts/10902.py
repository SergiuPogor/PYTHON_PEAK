import copy

# Define a nested object
original_data = {
    'name': 'Alice',
    'age': 30,
    'skills': ['Python', 'Data Analysis'],
    'projects': {
        'project1': ['Task 1', 'Task 2'],
        'project2': ['Task A', 'Task B']
    }
}

# Create a deep copy of the original nested object
copied_data = copy.deepcopy(original_data)

# Modifying the copied data to show independence from the original
copied_data['skills'].append('Machine Learning')
copied_data['projects']['project1'].append('Task 3')

# Display the results
print("Original Data:")
print(original_data)
print("\nCopied Data:")
print(copied_data)