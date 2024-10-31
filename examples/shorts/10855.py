import traceback

def risky_function():
    # This function may raise an error
    return 10 / 0  # Division by zero error

def main():
    try:
        risky_function()
    except Exception as e:
        # Log the full traceback for debugging
        error_message = traceback.format_exc()
        print("An error occurred:")
        print(error_message)

if __name__ == "__main__":
    main()