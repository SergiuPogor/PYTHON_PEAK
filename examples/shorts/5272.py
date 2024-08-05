# Function to sort a list of dictionaries by a specific key
def sort_by_key(data, sort_key):
    return sorted(data, key=lambda x: x[sort_key])

# Function to sort a list of objects by a specific attribute
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

def sort_students(students, attr):
    return sorted(students, key=lambda x: getattr(x, attr))

def main():
    # Example data: list of dictionaries
    students_dict = [
        {"name": "Alice", "score": 90},
        {"name": "Bob", "score": 75},
        {"name": "Charlie", "score": 85}
    ]
    
    # Sort by score
    sorted_students = sort_by_key(students_dict, 'score')
    print("Sorted by score (dict):", sorted_students)
    
    # Example data: list of Student objects
    students_obj = [
        Student("Alice", 90),
        Student("Bob", 75),
        Student("Charlie", 85)
    ]
    
    # Sort by score attribute
    sorted_students_obj = sort_students(students_obj, 'score')
    print("Sorted by score (objects):", sorted_students_obj)

if __name__ == "__main__":
    main()
