from typing import List, Dict, Union

def calculate_average(grades: List[Union[int, float]]) -> float:
    """Calculate the average of a list of grades."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def student_summary(name: str, age: int, grades: List[Union[int, float]]) -> Dict[str, Union[str, int, float]]:
    """Return a summary of a student's information."""
    average_grade = calculate_average(grades)
    return {
        "name": name,
        "age": age,
        "average_grade": average_grade
    }

def main():
    # Define a list of students with grades
    students = [
        student_summary("Alice", 21, [85, 90, 88]),
        student_summary("Bob", 22, [78, 82, 80]),
        student_summary("Charlie", 20, [90, 92, 94])
    ]

    # Print the summary of each student
    for student in students:
        print(student)

if __name__ == "__main__":
    main()