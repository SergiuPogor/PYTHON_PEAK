# Example Python code demonstrating advanced usage of the sort() method with a custom key function

# Suppose we have a list of dictionaries representing people with their names and ages
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# We want to sort by age first, and if ages are the same, sort by name
people.sort(key=lambda person: (person['age'], person['name']))

# Output the sorted list
for person in people:
    print(person)