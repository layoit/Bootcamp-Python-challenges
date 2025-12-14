def check_leap_year():
    print("Coding Challenge 9: Check Leap Year")
    try:
        year = int(input("Enter a year: "))
        
        # Leap year logic:
        # Divisible by 4 AND (not divisible by 100 OR divisible by 400)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is NOT a Leap Year.")
    except ValueError:
        print("Invalid input! Please enter a valid year (integer).")

if __name__ == "__main__":
    check_leap_year()
