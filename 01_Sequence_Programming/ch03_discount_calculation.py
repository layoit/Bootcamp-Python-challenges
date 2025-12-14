def calculate_discount():
    print("Coding Challenge 3: Calculate Discount")
    try:
        total_amount = float(input("Enter Total Amount: "))
        discount_percentage = float(input("Enter Discount Percentage: "))
        
        discount_amount = (total_amount * discount_percentage) / 100
        final_amount = total_amount - discount_amount
        
        print(f"Discount Amount: {discount_amount}")
        print(f"Final Amount to Pay: {final_amount}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculate_discount()
