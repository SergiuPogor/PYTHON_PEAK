# Efficient ways to reverse a string in Python

# Common use case - Reversing a string
# Example 1: Using slicing - Most efficient and recommended
s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)  # Output: !dlrow ,olleH

# Example 2: Reversing using a loop (NOT recommended for performance)
def reverse_string_loop(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string_loop(s))  # Output: !dlrow ,olleH

# Example 3: Using `reversed()` and `''.join()` (less efficient for large strings)
reversed_s_alt = ''.join(reversed(s))
print(reversed_s_alt)  # Output: !dlrow ,olleH

# Real-world use case: Reversing file contents
input_file_path = '/tmp/test/input.txt'
output_file_path = '/tmp/test/reversed_output.txt'

# Read the file contents, reverse it, and save the reversed contents into a new file
with open(input_file_path, 'r') as input_file:
    content = input_file.read()

reversed_content = content[::-1]

with open(output_file_path, 'w') as output_file:
    output_file.write(reversed_content)

# Example 4: Reverse a list (slicing works here too)
sample_list = [1, 2, 3, 4, 5]
reversed_list = sample_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]

# Example 5: Using slicing to reverse in place for mutable sequences (e.g., lists)
# Reversing a list in-place
mutable_list = [10, 20, 30, 40, 50]
mutable_list[:] = mutable_list[::-1]
print(mutable_list)  # Output: [50, 40, 30, 20, 10]

# Fun fact: Slicing even works on strings containing Unicode characters
unicode_str = "Python 🐍 is fun!"
reversed_unicode = unicode_str[::-1]
print(reversed_unicode)  # Output: !nuf si 🐍 nohtyP

# Bonus: Reverse the words in a sentence (but not the characters)
sentence = "Reverse only the words in this sentence"
reversed_words = ' '.join(sentence.split()[::-1])
print(reversed_words)  # Output: sentence this in words the only Reverse

# Conclusion: The slice notation `[::-1]` is a powerful, fast, and Pythonic way to reverse any sequence, 
# whether it's a string, list, or even a Unicode text!