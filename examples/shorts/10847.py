def check_conditions(values):
    # Check if at least one value is True
    if any(values):
        print("At least one condition is True!")
    else:
        print("All conditions are False.")

def check_all_conditions(values):
    # Check if all values are True
    if all(values):
        print("All conditions are True!")
    else:
        print("At least one condition is False.")

def main():
    conditions = [True, False, True]
    check_conditions(conditions)
    
    all_conditions = [True, True, True]
    check_all_conditions(all_conditions)

if __name__ == "__main__":
    main()