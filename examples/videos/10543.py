from typing import List, Dict, Tuple, Union, Optional

# A sample function to calculate student scores, with type annotations for clarity
def calculate_scores(student_data: Dict[str, List[Tuple[str, int]]]) -> Dict[str, Union[int, float]]:
    results = {}
    for student, exams in student_data.items():
        total_score = sum(score for _, score in exams)
        results[student] = round(total_score / len(exams), 2)
    return results

# Example usage of calculate_scores with type-annotated dictionary input
students = {
    "Alice": [("Math", 85), ("Science", 90), ("English", 78)],
    "Bob": [("Math", 72), ("Science", 88), ("English", 91)],
    "Charlie": [("Math", 94), ("Science", 85), ("English", 80)]
}

# Calculate and print average scores for each student
print("Student Average Scores:")
for student, average in calculate_scores(students).items():
    print(f"  {student}: {average}")

# A function with type annotations to filter a list of numbers, optionally with a minimum threshold
def filter_numbers(numbers: List[int], min_value: Optional[int] = None) -> List[int]:
    return [num for num in numbers if min_value is None or num >= min_value]

# Using the filter_numbers function to filter numbers with and without the min_value parameter
numbers = [5, 12, 7, 18, 3, 9, 21]
print("\nFiltered Numbers:")
print("  Without min_value:", filter_numbers(numbers))
print("  With min_value=10:", filter_numbers(numbers, min_value=10))

# An advanced function demonstrating type annotations for a file parsing example
def parse_data_file(file_path: str) -> Dict[str, Union[str, int]]:
    parsed_data = {}
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or "=" not in line:  # Skip blank lines or malformed lines
                continue
            try:
                key, value = line.split("=", 1)  # Split only on the first '='
                parsed_data[key] = int(value) if value.isdigit() else value
            except ValueError:
                print(f"Skipping malformed line: {line}")
    return parsed_data

# Testing parse_data_file function with a sample data file
test_file_path = '/tmp/test/input.txt'
parsed_content = parse_data_file(test_file_path)
print("\nParsed Data from File:")
for key, value in parsed_content.items():
    print(f"  {key}: {value}")

# Function combining multiple type annotations, demonstrating Optional, Union, and complex return types
def get_student_report(name: str, scores: Optional[Dict[str, int]] = None) -> Union[str, Dict[str, float]]:
    if scores is None:
        return f"No scores available for {name}."
    average_score = sum(scores.values()) / len(scores)
    return {"name": name, "average_score": round(average_score, 2)}

# Example usage of get_student_report
print("\nStudent Report:")
print(get_student_report("Alice", {"Math": 88, "Science": 92}))
print(get_student_report("Eve"))

