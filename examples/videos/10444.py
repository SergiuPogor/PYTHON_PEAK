class Person:
    def __init__(self, name):
        self.name = name

# Create two instances with the same name
person1 = Person("Alice")
person2 = Person("Alice")

# Create a reference to person1
person3 = person1

# Use 'is' to check object identity
print(person1 is person2)  # Output: False (different objects)
print(person1 is person3)  # Output: True (same object)

# Use '==' to check value equality
print(person1 == person2)  # Output: False (different instances)
print(person1.name == person2.name)  # Output: True (same value)

# Example of a common mistake
list1 = [1, 2, 3]
list2 = list1

# Check identity and equality
print(list1 is list2)  # Output: True (same object)
print(list1 == list2)  # Output: True (same values)

# Modify list2 and see the effect
list2.append(4)

print(list1)  # Output: [1, 2, 3, 4] (list1 changed)
print(list2)  # Output: [1, 2, 3, 4]

# Create a new list with the same values
list3 = [1, 2, 3]

# Check identity and equality
print(list1 is list3)  # Output: False (different objects)
print(list1 == list3)  # Output: False (different values)