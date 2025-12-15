def ch51_input_level0():
    print("Coding Challenge 51: Accept n and store elements (Level 0)")
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
    ch51_input_level0()
