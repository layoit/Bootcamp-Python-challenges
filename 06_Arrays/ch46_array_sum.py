def ch46_sum_array():
    print("Coding Challenge 46: Sum of all elements (Level 1)")
    try:
        n = int(input("Enter size of array (n): "))
        arr = []
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
        
        # Manual Sum
        total = 0
        for x in arr:
            total += x
            
        print(f"Sum of elements: {total}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    ch46_sum_array()
