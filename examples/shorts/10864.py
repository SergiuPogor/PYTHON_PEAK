# Merging dictionaries using dict.update()
def merge_dictionaries(dict1, dict2):
    # Create a copy of the first dictionary
    merged_dict = dict1.copy()
    # Merge the second dictionary into the first
    merged_dict.update(dict2)
    return merged_dict

def main():
    # Sample dictionaries
    user_info = {
        'name': 'Alice',
        'age': 30
    }
    contact_info = {
        'email': 'alice@example.com',
        'age': 31  # This will overwrite age in user_info
    }

    # Merging dictionaries
    final_info = merge_dictionaries(user_info, contact_info)

    # Display the merged dictionary
    print("Merged Dictionary:", final_info)

if __name__ == "__main__":
    main()