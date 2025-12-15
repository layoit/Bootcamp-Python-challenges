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

def challenge_60():
    print("--- Challenge 60: Multiply Two Matrices ---")
    try:
        print("Matrix A details:")
        rows_a = int(input("Enter rows for Matrix A: "))
        cols_a = int(input("Enter cols for Matrix A: "))
        matrix_a = input_matrix(rows_a, cols_a, "A")
        
        print("\nMatrix B details:")
        rows_b = int(input("Enter rows for Matrix B: "))
        cols_b = int(input("Enter cols for Matrix B: "))
        
        if cols_a != rows_b:
            print("Multiplication not possible! Cols of A must match Rows of B.")
        else:
            matrix_b = input_matrix(rows_b, cols_b, "B")
            
            print("\nMatrix A:")
            print_matrix(matrix_a)
            print("Matrix B:")
            print_matrix(matrix_b)
            
            # Result dimension will be rows_a x cols_b
            result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
            
            for i in range(rows_a):
                for j in range(cols_b):
                    for k in range(cols_a): # Iterate over common dimension
                        result[i][j] += matrix_a[i][k] * matrix_b[k][j]
            
            print("\nProduct of A and B:")
            print_matrix(result)
            
    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    challenge_60()
