def ch45_input_array():
    print("Coding Challenge 45: Accept n and store elements (Level 0)")
    try:
        n = int(input("Enter size of array (n): "))
        print(f"Enter {n} integers:")
        arr = []
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
        
        print("Stored Array:", arr)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    ch45_input_array()
