def ch47_min_array():
    print("Coding Challenge 47: Find Minimum value (Level 2)")
    try:
        n = int(input("Enter size of array (n): "))
        if n <= 0:
            print("Size must be positive.")
            return

        arr = []
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
        
        # Manual Min
        min_val = arr[0]
        for x in arr:
            if x < min_val:
                min_val = x
                
        print(f"Minimum value: {min_val}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    ch47_min_array()
