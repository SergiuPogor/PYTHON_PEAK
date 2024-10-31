class DynamicAttributes:
    def __init__(self, name):
        self.name = name

    def add_attribute(self, attr_name, value):
        setattr(self, attr_name, value)

    def display_attributes(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

def main():
    # Create an instance of DynamicAttributes
    person = DynamicAttributes("Alice")

    # Add dynamic attributes
    person.add_attribute("age", 30)
    person.add_attribute("city", "New York")

    # Display all attributes
    person.display_attributes()

    # Add more attributes dynamically
    person.add_attribute("profession", "Engineer")
    person.add_attribute("hobbies", ["Reading", "Traveling"])

    # Display updated attributes
    print("\nUpdated Attributes:")
    person.display_attributes()

if __name__ == "__main__":
    main()