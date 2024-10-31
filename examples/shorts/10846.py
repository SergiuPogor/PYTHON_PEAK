import pdb

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Negative numbers do not have a factorial.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    try:
        # Set a breakpoint here
        pdb.set_trace()
        number = 5
        factorial = calculate_factorial(number)
        print(f"Factorial of {number} is {factorial}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()