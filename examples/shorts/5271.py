class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

def update_person_info(person, attribute_name, value):
    setattr(person, attribute_name, value)

def main():
    # Create a person instance
    person = Person("Alice", 30)
    print(person)  # Output: Alice, Age: 30
    
    # Update the person's name
    update_person_info(person, 'name', 'Bob')
    # Update the person's age
    update_person_info(person, 'age', 35)
    
    print(person)  # Output: Bob, Age: 35

if __name__ == "__main__":
    main()
