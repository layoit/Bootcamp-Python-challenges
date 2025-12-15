def reverse_number():
    print("Coding Challenge 44: Reverse of a Number (Math Logic)")
    try:
        num = int(input("Enter a number: "))
        original = num
        rev = 0
        
        temp = abs(num)
        while temp > 0:
            digit = temp % 10
            rev = (rev * 10) + digit
            temp = temp // 10
            
        if num < 0:
            rev = -rev
            
        print(f"Original: {original}")
        print(f"Reverse: {rev}")
        
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    reverse_number()
