class Person:
    def __init__(self, name, age):
        self._name = name  # private attribute
        self._age = age    # private attribute

    @property
    def name(self):
        """Get the person's name."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Set the person's name with validation."""
        if isinstance(new_name, str) and new_name:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def age(self):
        """Get the person's age."""
        return self._age

    @age.setter
    def age(self, new_age):
        """Set the person's age with validation."""
        if isinstance(new_age, int) and 0 <= new_age <= 120:
            self._age = new_age
        else:
            raise ValueError("Age must be an integer between 0 and 120")

# Example usage
if __name__ == "__main__":
    # Create a new person
    person = Person("Alice", 30)
    
    # Display the person's details
    print(f"Name: {person.name}, Age: {person.age}")
    
    # Update the name and age
    person.name = "Bob"
    person.age = 35
    print(f"Updated Name: {person.name}, Updated Age: {person.age}")
    
    # Attempting to set invalid age
    try:
        person.age = -5  # This should raise an error
    except ValueError as e:
        print("Error:", e)