def check_conditions(conditions):
    # Using any() to check if at least one condition is True
    if any(conditions):
        print("At least one condition is true!")
    else:
        print("No conditions are true.")
        
    # Using all() to check if all conditions are True
    if all(conditions):
        print("All conditions are true!")
    else:
        print("Not all conditions are true.")

def main():
    conditions = [True, False, True]  # Example conditions
    check_conditions(conditions)

if __name__ == "__main__":
    main()