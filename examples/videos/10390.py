# This script demonstrates how to use SortedList from sortedcontainers
# for fast insertions while maintaining order.

from sortedcontainers import SortedList

def main():
    # Create a SortedList instance
    sorted_list = SortedList()

    # Sample data to insert
    data_to_insert = [5, 3, 8, 1, 4]

    # Inserting elements
    for item in data_to_insert:
        sorted_list.add(item)
        print(f"Inserted {item}: {sorted_list}")

    # Inserting a new element
    new_element = 2
    sorted_list.add(new_element)
    print(f"Inserted {new_element}: {sorted_list}")

    # Inserting a larger number
    larger_element = 10
    sorted_list.add(larger_element)
    print(f"Inserted {larger_element}: {sorted_list}")

    # Final state of the sorted list
    print("Final sorted list:", sorted_list)

if __name__ == "__main__":
    main()