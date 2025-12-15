def ch48_max_array():
    print("Coding Challenge 48: Find Maximum value (Level 3)")
    try:
        n = int(input("Enter size of array (n): "))
        if n <= 0:
            print("Size must be positive.")
            return

        arr = []
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
        
        # Manual Max
        max_val = arr[0]
        for x in arr:
            if x > max_val:
                max_val = x
                
        print(f"Maximum value: {max_val}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    ch48_max_array()
