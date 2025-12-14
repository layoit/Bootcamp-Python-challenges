def calculate_sum_average():
    print("Coding Challenge 1: Find Sum and Average of Two Variables")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        total = num1 + num2
        average = total / 2
        
        print(f"Sum: {total}")
        print(f"Average: {average}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculate_sum_average()
