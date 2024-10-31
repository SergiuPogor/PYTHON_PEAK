def append_item(item, my_list=None):
    # Use None to create a new list if not provided
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

def main():
    # First call with a new list
    print(append_item("apple"))  # Output: ['apple']

    # Second call with a new item, should not share list
    print(append_item("banana"))  # Output: ['banana']

    # Call with existing list
    existing_list = ['orange']
    print(append_item("grape", existing_list))  # Output: ['orange', 'grape']

if __name__ == "__main__":
    main()