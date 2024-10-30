# Using enumerate to track index in a list
fruits = ['apple', 'banana', 'cherry', 'date']

# Using enumerate in a for loop
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Example with conditional logic
for index, fruit in enumerate(fruits):
    if index % 2 == 0:  # Only print even indexed fruits
        print(f"Even Index - {index}: {fruit}")

# Creating a dictionary with index as key and fruit as value
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
print(fruit_dict)

# Using enumerate with a start index
for index, fruit in enumerate(fruits, start=1):
    print(f"Fruit {index}: {fruit}")