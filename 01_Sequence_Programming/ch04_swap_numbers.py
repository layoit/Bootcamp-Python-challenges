def swap_numbers():
    print("Coding Challenge 4: Swap Two Numbers")
    try:
        a = input("Enter value of A: ")
        b = input("Enter value of B: ")
        
        print(f"Before Swapping: A = {a}, B = {b}")
        
        temp = a
        a = b
        b = temp
        
        print(f"After Swapping: A = {a}, B = {b}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    swap_numbers()
