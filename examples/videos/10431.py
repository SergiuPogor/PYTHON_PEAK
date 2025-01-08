from collections import namedtuple

# Define a namedtuple to represent a Person
Person = namedtuple('Person', ['name', 'age', 'city'])

def create_person(name, age, city):
    # Create a new Person instance
    return Person(name, age, city)

def display_person(person):
    # Display person's information
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    print(f"City: {person.city}")

# Example usage
def main():
    # Create multiple persons
    people = [
        create_person("Alice", 30, "New York"),
        create_person("Bob", 25, "Los Angeles"),
        create_person("Charlie", 35, "Chicago")
    ]

    # Display information for each person
    for person in people:
        display_person(person)
        print("-" * 20)

    # Return the list of people to be used elsewhere
    return people

# Additional functionality: Calculate average age
def average_age(people):
    total_age = sum(person.age for person in people)
    return total_age / len(people)

if __name__ == "__main__":
    # Get the people list from main
    people = main()

    # Display the average age
    avg_age = average_age(people)
    print(f"Average Age: {avg_age:.2f}")

