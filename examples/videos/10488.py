import pickle

class Student:
    """Class to represent a student."""
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, grades={self.grades})"

def save_students(students, filename):
    """Save student objects to a file using pickle."""
    with open(filename, 'wb') as file:
        pickle.dump(students, file)

def load_students(filename):
    """Load student objects from a pickle file."""
    with open(filename, 'rb') as file:
        return pickle.load(file)

def main():
    # Create a list of Student objects
    students = [
        Student("Alice", 21, [85, 90, 88]),
        Student("Bob", 22, [78, 82, 80]),
        Student("Charlie", 20, [90, 92, 94])
    ]

    # Save the list of students to a file
    save_students(students, '/tmp/test/students.pkl')

    # Load the list of students back from the file
    loaded_students = load_students('/tmp/test/students.pkl')
    
    print("Loaded Students:")
    for student in loaded_students:
        print(student)

if __name__ == "__main__":
    main()