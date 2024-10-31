import pdb

def divide_numbers(a, b):
    # Start debugging session
    pdb.set_trace()
    return a / b

def main():
    try:
        result = divide_numbers(10, 0)  # Intentional error
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()