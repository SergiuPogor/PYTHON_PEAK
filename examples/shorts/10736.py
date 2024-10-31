def check_conditions(conditions):
    if any(conditions):
        print("At least one condition is true!")
    else:
        print("No conditions are true.")

    if all(conditions):
        print("All conditions are true!")
    else:
        print("Not all conditions are true.")

# Example usage
conditions_list = [False, False, True, False]
check_conditions(conditions_list)  # Output: At least one condition is true! Not all conditions are true!