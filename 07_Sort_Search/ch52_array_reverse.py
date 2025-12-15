def ch52_reverse_array():
    print("Coding Challenge 52: Reverse the given array (Level 1)")
    try:
        n = int(input("Enter size of array (n): "))
        arr = []
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
            
        print("Original:", arr)
        
        # Manual Reverse (Two-Pointer Swap)
        start = 0
        end = len(arr) - 1
        while start < end:
            # Swap
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            
            start += 1
            end -= 1
            
        print("Reversed:", arr)
        
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    ch52_reverse_array()
