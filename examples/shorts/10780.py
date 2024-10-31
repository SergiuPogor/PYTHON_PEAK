# Example of using any() and all() in Python

# Sample data: list of user ages
user_ages = [22, 18, 17, 25]

# Check if at least one user is an adult (18 or older)
is_any_adult = any(age >= 18 for age in user_ages)
print("Is there at least one adult?", is_any_adult)

# Check if all users are adults
are_all_adults = all(age >= 18 for age in user_ages)
print("Are all users adults?", are_all_adults)

# Sample conditions: user preferences
preferences = [True, False, True]

# Check if any preferences are true
has_any_preference = any(preferences)
print("Is there any preference selected?", has_any_preference)

# Check if all preferences are true
are_all_preferences = all(preferences)
print("Are all preferences selected?", are_all_preferences)