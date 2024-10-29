from collections import Counter

def analyze_text_frequency(text):
    # Normalize the text to lower case
    text = text.lower()
    
    # Split the text into words
    words = text.split()
    
    # Use Counter to count the frequency of each word
    frequency = Counter(words)
    
    return frequency

def analyze_data_frequency(data):
    # Use Counter to count the frequency of each item in a list
    frequency = Counter(data)
    
    return frequency

# Example usage of analyze_text_frequency
text_data = "Python is great and python is fun. Python is powerful!"
text_frequency = analyze_text_frequency(text_data)

print("Word Frequency in Text:")
for word, count in text_frequency.items():
    print(f"{word}: {count}")

# Example usage of analyze_data_frequency
list_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
list_frequency = analyze_data_frequency(list_data)

print("\nItem Frequency in List:")
for item, count in list_frequency.items():
    print(f"{item}: {count}")