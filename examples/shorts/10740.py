import pdb

def faulty_function():
    total = 0
    for i in range(5):
        total += i
        # Introduce a bug on purpose
        if i == 3:
            total += "string"  # This will raise a TypeError
    return total

def main():
    pdb.set_trace()  # Start the debugger here
    result = faulty_function()
    print(f"Result is {result}")

if __name__ == "__main__":
    main()  # Run the main function to start debugging