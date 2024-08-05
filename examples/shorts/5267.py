def calculate_power(base, exp, mod=None):
    if mod is None:
        # Calculate base raised to the power exp
        return pow(base, exp)
    else:
        # Calculate (base ** exp) % mod efficiently
        return pow(base, exp, mod)

def main():
    base = 7
    exponent = 1234
    modulus = 100000

    # Example of large exponentiation without modulus
    result_no_mod = calculate_power(base, exponent)
    print(f"Result without modulus: {result_no_mod}")

    # Example of large exponentiation with modulus
    result_with_mod = calculate_power(base, exponent, modulus)
    print(f"Result with modulus: {result_with_mod}")

if __name__ == "__main__":
    main()
