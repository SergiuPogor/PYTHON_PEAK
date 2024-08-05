# Example class to demonstrate the use of vars()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            # Use vars() to update instance attributes dynamically
            if key in vars(self):
                setattr( self, key, value)
            else:
                print(f"Attribute '{key}' does not exist.")

    def display_info(self):
        # Use vars() to access and print instance attributes
        info = vars(self)
        for key, value in info.items():
            print(f"{key}: {value}")

def main():
    # Create a Person object
    person = Person("Alice", 30)
    
    # Display initial info
    person.display_info()
    
    # Update attributes dynamically
    person.update_info(name="Bob", age=35, city="New York")
    
    # Display updated info
    person.display_info()

if __name__ == "__main__":
    main()


