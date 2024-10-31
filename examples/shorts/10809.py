# Example of using setdefault to initialize a nested dictionary
def initialize_student_grades():
    # Creating an empty dictionary for students
    student_grades = {}

    # List of students
    students = ["Alice", "Bob", "Charlie"]

    # Initializing grades for each student
    for student in students:
        student_grades.setdefault(student, [])
        student_grades[student].append(0)  # Start each student with a grade of 0

    return student_grades

# Display initialized student grades
grades = initialize_student_grades()
print(grades)  # {'Alice': [0], 'Bob': [0], 'Charlie': [0]}

# Example of using setdefault for counting occurrences
def count_word_occurrences(words):
    word_count = {}
    for word in words:
        word_count.setdefault(word, 0)
        word_count[word] += 1  # Increment count for the word

    return word_count

# List of words
word_list = ["apple", "banana", "apple", "orange", "banana", "banana"]
word_occurrences = count_word_occurrences(word_list)
print(word_occurrences)  # {'apple': 2, 'banana': 3, 'orange': 1}