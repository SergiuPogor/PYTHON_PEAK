# Using list comprehensions to simplify code

# Sample data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension to create a new list of squares
squares = [num ** 2 for num in numbers]

# Filtering even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Creating a dictionary from two lists using dictionary comprehension
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {key: value for key, value in zip(keys, values)}

# Function to create a list of tuples (number, square)
def number_square_tuples(nums):
    return [(num, num ** 2) for num in nums]

# Main function to demonstrate list comprehensions
def main():
    print("Squares:", squares)
    print("Even Numbers:", even_numbers)
    print("Dictionary:", my_dict)
    print("Number and Square Tuples:", number_square_tuples(numbers))

# Uncomment to run the main function
# if __name__ == "__main__":
#     main()