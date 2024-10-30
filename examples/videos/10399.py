from collections import defaultdict

def count_fruits(fruit_list):
    """Count occurrences of each fruit in the list."""
    fruit_count = defaultdict(int)
    
    for fruit in fruit_list:
        fruit_count[fruit] += 1
    
    return fruit_count

def group_students_by_grade(students):
    """Group students by their grades."""
    grade_groups = defaultdict(list)
    
    for name, grade in students:
        grade_groups[grade].append(name)
    
    return grade_groups

def main():
    # Example data
    fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    student_data = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A'), ('David', 'C')]

    # Count fruits
    fruit_counts = count_fruits(fruits)
    print("Fruit Counts:", dict(fruit_counts))

    # Group students by grade
    grouped_students = group_students_by_grade(student_data)
    print("Grouped Students:", dict(grouped_students))

if __name__ == "__main__":
    main()