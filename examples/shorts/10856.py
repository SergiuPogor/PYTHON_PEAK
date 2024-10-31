def reverse_string(s):
    # Efficiently reverse a string using slicing
    return s[::-1]

def main():
    input_string = "Hello, World!"
    reversed_string = reverse_string(input_string)
    print("Original String:", input_string)
    print("Reversed String:", reversed_string)

if __name__ == "__main__":
    main()