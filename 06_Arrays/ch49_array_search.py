def ch49_search_array():
    print("Coding Challenge 49: Search element (Level 4)")
    try:
        n = int(input("Enter size of array (n): "))
        arr = []
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
        
        target = int(input("Enter element to search: "))
        
        # Manual Search
        found = False
        index = -1
        
        for i in range(len(arr)):
            if arr[i] == target:
                found = True
                index = i
                break # Stop at first occurrence
        
        if found:
            print(f"Element {target} found at index {index}.")
        else:
            print("Element not found.")
            
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    ch49_search_array()
