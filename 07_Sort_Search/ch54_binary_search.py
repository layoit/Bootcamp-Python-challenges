def ch54_binary_search():
    print("Coding Challenge 54: Binary Search (Level 3)")
    try:
        n = int(input("Enter size of array (n): "))
        arr = []
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
            
        print("Original:", arr)
        
        # Step 1: Manual Sort 
        length = len(arr)
        for i in range(length):
            min_idx = i
            for j in range(i+1, length):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            # Swap
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
            
        print("Sorted for Search:", arr)
        
        # Step 2: Binary Search
        target = int(input("Enter element to search: "))
        
        low = 0
        high = length - 1
        found = False
        index = -1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                found = True
                index = mid
                break
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if found:
            print(f"Element {target} found at index {index}.")
        else:
            print("Element not found.")
            
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    ch54_binary_search()
