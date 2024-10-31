def process_data(value):
    if value < 0:
        raise ValueError("Negative value error")
    elif value == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return 10 / value

def main():
    test_values = [10, 0, -5]
    
    for val in test_values:
        try:
            result = process_data(val)
            print(f"Result: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()  # Run the main function