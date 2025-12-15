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

def challenge_56():
    print("--- Challenge 56: Sum of all elements in 2D Array ---")
    try:
        rows = int(input("Enter number of rows (M): "))
        cols = int(input("Enter number of columns (N): "))
        
        matrix = input_matrix(rows, cols, "A")
        
        total_sum = sum(sum(row) for row in matrix)
        print(f"\nSum of all elements: {total_sum}")
        
    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    challenge_56()
