from itertools import product

def generate_cartesian_product(*args):
    # Generate the Cartesian product of input lists
    return list(product(*args))

def main():
    list1 = [1, 2]
    list2 = ['A', 'B']
    list3 = ['X', 'Y']

    cartesian_result = generate_cartesian_product(list1, list2, list3)
    
    for combination in cartesian_result:
        print(combination)

if __name__ == "__main__":
    main()