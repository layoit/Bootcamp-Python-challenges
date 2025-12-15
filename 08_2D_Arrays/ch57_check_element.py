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

def challenge_57():
    print("--- Challenge 57: Check if Element Exists in 2D Array ---")
    try:
        rows = int(input("Enter number of rows (M): "))
        cols = int(input("Enter number of columns (N): "))
        
        matrix = input_matrix(rows, cols, "A")
        
        search_val = int(input("Enter element to search: "))
        found = False
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == search_val:
                    print(f"Element {search_val} found at [{i}][{j}]")
                    found = True
        
        if not found:
            print("Element not found.")
            
    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    challenge_57()
