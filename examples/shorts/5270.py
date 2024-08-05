def calculate_salary(base_salary, bonus_percentage):
    # Calculate bonus amount
    bonus_amount = base_salary * (bonus_percentage / 100)
    # Calculate total salary with rounding
    total_salary = round(base_salary + bonus_amount, 2)
    return total_salary

def main():
    # Example base salary and bonus percentage
    base_salary = 4567.894
    bonus_percentage = 5.678
    
    # Calculate and print total salary
    print(f"Total Salary: ${calculate_salary(base_salary, bonus_percentage)}")

if __name__ == "__main__":
    main()

