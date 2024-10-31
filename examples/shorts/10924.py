# Example of using enumerate with a starting index of 1
items = ['apple', 'banana', 'cherry', 'date']

# Using enumerate to get indices starting from 1
for index, item in enumerate(items, start=1):
    print(f"Item {index}: {item}")

# Demonstrating with a more complex structure
student_scores = {'Alice': 88, 'Bob': 92, 'Charlie': 85}

# Displaying scores with enumerate starting from 1
for index, (student, score) in enumerate(student_scores.items(), start=1):
    print(f"Rank {index}: {student} scored {score}")

# Using enumerate to iterate over a range
for index in range(1, 6):
    print(f"Count: {index}")