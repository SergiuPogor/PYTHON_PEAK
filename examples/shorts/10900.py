def transpose_2d_list(matrix):
    # Using zip to transpose the matrix
    transposed = list(zip(*matrix))  # Transpose the matrix
    return transposed

# Example usage
if __name__ == "__main__":
    original_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    transposed_matrix = transpose_2d_list(original_matrix)
    
    # Display the results
    print("Original Matrix:")
    for row in original_matrix:
        print(row)
    
    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(row)