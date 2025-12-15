def input_matrix(rows, cols, name="Matrix"):
    print(f"Enter elements for {name} ({rows}x{cols}):")
    mat = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Try/except block to handle non-integer inputs gracefully could be added,
            # but keeping it simple as per original style.
            val = int(input(f"Element [{i}][{j}]: "))
            row.append(val)
        mat.append(row)
    return mat

def print_matrix(mat):
    for row in mat:
        print(*row)

def challenge_55():
    print("--- Challenge 55: Create and Display 2D Array ---")
    try:
        rows = int(input("Enter number of rows (M): "))
        cols = int(input("Enter number of columns (N): "))
        
        matrix = input_matrix(rows, cols, "A")
        
        print("\nMatrix Elements (Row-wise):")
        print_matrix(matrix)
        
    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    challenge_55()
