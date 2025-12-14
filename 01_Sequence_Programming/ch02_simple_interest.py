def calculate_simple_interest():
    print("Coding Challenge 2: Calculate Simple Interest")
    try:
        principal = float(input("Enter Principal Amount: "))
        rate = float(input("Enter Rate of Interest (%): "))
        time = float(input("Enter Time Period (in years): "))
        
        simple_interest = (principal * rate * time) / 100
        
        print(f"Simple Interest: {simple_interest}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculate_simple_interest()
