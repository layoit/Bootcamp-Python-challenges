def input_matrix(rows, cols, name="Matrix"):
    print(f"Enter elements for {name} ({rows}x{cols}):")
    mat = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Element [{i}][{j}]: "))
            row.append(val)
        mat.append(row)
    return mat

def print_matrix(mat):
    for row in mat:
        print(*row)

def challenge_58_59():
    print("--- Challenge 58 & 59: Matrix Transpose ---")
    try:
        rows = int(input("Enter number of rows (M): "))
        cols = int(input("Enter number of columns (N): "))
        
        matrix = input_matrix(rows, cols, "A")
        
        print("\nOriginal Matrix:")
        print_matrix(matrix)
        
        # Transpose logic: Swap rows with columns
        # New dimensions will be cols x rows
        transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
        
        print("\nTranspose of Matrix:")
        print_matrix(transpose)
            
    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    challenge_58_59()
