def ch50_count_odd_even():
    print("Coding Challenge 50: Count Odd and Even numbers (Level 5)")
    try:
        n = int(input("Enter size of array (n): "))
        arr = []
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
        
        # Manual Count
        odd_count = 0
        even_count = 0
        
        for x in arr:
            if x % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
        print(f"Odd numbers count: {odd_count}")
        print(f"Even numbers count: {even_count}")
            
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    ch50_count_odd_even()
