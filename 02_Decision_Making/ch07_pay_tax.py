def check_tax_status():
    print("Coding Challenge 7: Check Tax Status")
    try:
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))
        
        if salary > 300000:
            print(f"Mr./Ms. {name}, your salary is {salary}. You must pay tax.")
        else:
            print(f"Mr./Ms. {name}, your salary is {salary}. You do not need to pay tax.")
    except ValueError:
        print("Invalid input! Please enter numeric values for salary.")

if __name__ == "__main__":
    check_tax_status()
