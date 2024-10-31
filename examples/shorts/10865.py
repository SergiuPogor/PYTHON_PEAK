from enum import Enum

# Define an Enum for days of the week
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def print_schedule(day):
    # Print different activities based on the day
    if day == Day.MONDAY:
        print("Start the week strong!")
    elif day == Day.FRIDAY:
        print("Prepare for the weekend!")
    elif day == Day.SATURDAY:
        print("Enjoy your day off!")
    else:
        print("It's a regular workday.")

def main():
    # Example of using enum
    today = Day.WEDNESDAY
    print("Today is:", today.name)
    print_schedule(today)

if __name__ == "__main__":
    main()