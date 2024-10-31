from itertools import zip_longest

def combine_lists(list1, list2, fill_value=None):
    # Use zip_longest to merge two lists
    combined = list(zip_longest(list1, list2, fillvalue=fill_value))
    return combined

# Example usage
if __name__ == "__main__":
    list_a = [1, 2, 3, 4]
    list_b = ['a', 'b']
    
    # Combine lists with 'None' as the fill value
    combined_lists = combine_lists(list_a, list_b, fill_value='None')
    
    # Display the results
    print("Combined Lists:")
    for pair in combined_lists:
        print(pair)