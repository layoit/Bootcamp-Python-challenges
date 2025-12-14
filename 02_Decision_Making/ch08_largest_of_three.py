def largest_of_three():
    print("Coding Challenge 8: Largest of 3 Numbers")
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        n3 = float(input("Enter third number: "))
        
        if n1 >= n2 and n1 >= n3:
            largest = n1
        elif n2 >= n1 and n2 >= n3:
            largest = n2
        else:
            largest = n3
            
        print(f"The largest number is: {largest}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    largest_of_three()
