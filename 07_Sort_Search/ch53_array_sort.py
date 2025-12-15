def ch53_sort_array():
    print("Coding Challenge 53: Sort array ascending/descending (Level 2)")
    try:
        n = int(input("Enter size of array (n): "))
        arr = []
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
            
        choice = input("Sort Order (1. Ascending, 2. Descending): ")
        
        # Manual Bubble Sort
        length = len(arr)
        for i in range(length):
            for j in range(0, length - i - 1):
                # Swap logic
                should_swap = False
                if choice == '1': # Ascending
                    if arr[j] > arr[j+1]:
                        should_swap = True
                elif choice == '2': # Descending
                    if arr[j] < arr[j+1]:
                        should_swap = True
                
                if should_swap:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

        if choice == '1':
            print("Sorted (Ascending):", arr)
        elif choice == '2':
            print("Sorted (Descending):", arr)
        else:
            print("Invalid choice.")
            
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    ch53_sort_array()
