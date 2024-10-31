import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_circular_linked_list():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # Creating a circular reference
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Circular reference

    return node1

def safe_deepcopy(obj):
    # Custom method to avoid infinite recursion
    seen = {}
    
    def recursive_copy(o):
        if id(o) in seen:
            return seen[id(o)]
        
        copy_obj = copy.copy(o)
        seen[id(o)] = copy_obj
        
        for attr, value in vars(o).items():
            setattr(copy_obj, attr, recursive_copy(value))
        
        return copy_obj
    
    return recursive_copy(obj)

if __name__ == "__main__":
    circular_list = create_circular_linked_list()
    
    # Attempt to deepcopy the circular linked list safely
    copied_list = safe_deepcopy(circular_list)
    
    print("Original head value:", circular_list.value)
    print("Copied head value:", copied_list.value)