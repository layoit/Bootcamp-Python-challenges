def check_even_odd():
    print("Coding Challenge 6: Check Even or Odd")
    try:
        num = int(input("Enter a number: "))
        
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    check_even_odd()
