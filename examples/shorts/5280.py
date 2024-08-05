from collections import defaultdict

def count_words(file_path):
    # Create a defaultdict with int as default factory
    word_count = defaultdict(int)
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count[word] += 1

    # Print word counts
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = '/tmp/test/input.txt'
    count_words(file_path)
