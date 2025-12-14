import sys

def validate_input(prompt, type_func, condition_func=None, error_msg="Invalid input."):
    while True:
        try:
            value = type_func(input(prompt))
            if condition_func and not condition_func(value):
                print(error_msg)
                continue
            return value
        except ValueError:
            print(error_msg)

def calculate_tax(taxable_income):


    tax = 0
    breakdown = []
    
    # 87A Rebate: Income <= 7,00,000 -> Tax is 0
    if taxable_income <= 700000:
        return 0, ["Rebate u/s 87A applied. Tax payable: 0"]
    
    remaining_income = taxable_income
    
    # Slab 1: 0 - 3L
    if remaining_income > 300000:
        breakdown.append("0 - 3L: 0%")
        # remaining_income does not change for calculation in next slab, we just take the difference
    else:
        breakdown.append("0 - 3L: 0%")
        return 0, breakdown

    # Slab 2: 3L - 6L (Max 3L @ 5% = 15000)
    if taxable_income > 300000:
        slab_amount = min(taxable_income, 600000) - 300000
        tax_slab = slab_amount * 0.05
        tax += tax_slab
        breakdown.append(f"3L - 6L: 5% on {slab_amount} = {tax_slab}")
    
    # Slab 3: 6L - 9L (Max 3L @ 10% = 30000)
    if taxable_income > 600000:
        slab_amount = min(taxable_income, 900000) - 600000
        tax_slab = slab_amount * 0.10
        tax += tax_slab
        breakdown.append(f"6L - 9L: 10% on {slab_amount} = {tax_slab}")

    # Slab 4: 9L - 12L (Max 3L @ 15% = 45000)
    if taxable_income > 900000:
        slab_amount = min(taxable_income, 1200000) - 900000
        tax_slab = slab_amount * 0.15
        tax += tax_slab
        breakdown.append(f"9L - 12L: 15% on {slab_amount} = {tax_slab}")

    # Slab 5: 12L - 15L (Max 3L @ 20% = 60000)
    if taxable_income > 1200000:
        slab_amount = min(taxable_income, 1500000) - 1200000
        tax_slab = slab_amount * 0.20
        tax += tax_slab
        breakdown.append(f"12L - 15L: 20% on {slab_amount} = {tax_slab}")

    # Slab 6: > 15L (Remaining @ 30%)
    if taxable_income > 1500000:
        slab_amount = taxable_income - 1500000
        tax_slab = slab_amount * 0.30
        tax += tax_slab
        breakdown.append(f"> 15L: 30% on {slab_amount} = {tax_slab}")
        
    return tax, breakdown

def main():
    print("--- Tax Calculator (Hackathon Challenges 11-16) ---")
    
    # Coding Challenge 16: Input Validation Rules
    name = validate_input("Enter Name: ", str, lambda x: x.replace(" ", "").isalpha() and len(x) > 0 and len(x) <= 50, "Name must be alphabets only and max 50 chars.")
    emp_id = validate_input("Enter EmpID (alphanumerate 5-10 chars): ", str, lambda x: x.isalnum() and 5 <= len(x) <= 10, "EmpID must be 5-10 alphanumeric characters.")
    basic_salary = validate_input("Enter Basic Monthly Salary: ", float, lambda x: 0 < x <= 10000000, "Basic Salary must be positive and <= 1,00,00,000.")
    special_allowances = validate_input("Enter Special Allowances (Monthly): ", float, lambda x: 0 <= x <= 10000000, "Special Allowances must be non-negative and <= 1,00,00,000.")
    bonus_percentage = validate_input("Enter Bonus Percentage (0-100): ", float, lambda x: 0 <= x <= 100, "Bonus percentage must be between 0 and 100.")
    
    # Coding Challenge 11: Basic Input and Salary Calculation
    gross_monthly_salary = basic_salary + special_allowances
    annual_gross_salary = (gross_monthly_salary * 12) * (1 + bonus_percentage / 100) 
    
    base_annual_salary = gross_monthly_salary * 12
    bonus_amount = base_annual_salary * (bonus_percentage / 100)
    annual_gross_salary = base_annual_salary + bonus_amount

    # Coding Challenge 12: Taxable Income Calculation
    standard_deduction = 50000
    taxable_income = max(0, annual_gross_salary - standard_deduction)
    
    # Coding Challenge 13: Tax and Rebate Calculation
    base_tax, tax_breakdown = calculate_tax(taxable_income)
    
    # Cess
    cess = base_tax * 0.04
    total_tax_payable = base_tax + cess
    
    # Coding Challenge 14: Net Salary Calculation
    annual_net_salary = annual_gross_salary - total_tax_payable
    
    # Coding Challenge 15: Report Generation
    print("\n" + "="*40)
    print(f"{'Employee Tax Report':^40}")
    print("="*40)
    print(f"{'Field':<25} | {'Details':<15}")
    print("-" * 43)
    print(f"{'Name':<25} | {name:<15}")
    print(f"{'EmpID':<25} | {emp_id:<15}")
    print(f"{'Gross Monthly Salary':<25} | Rs. {gross_monthly_salary:,.2f}")
    print(f"{'Annual Gross Salary':<25} | Rs. {annual_gross_salary:,.2f}")
    print(f"{'Standard Deduction':<25} | Rs. {standard_deduction:,.2f}")
    print(f"{'Taxable Income':<25} | Rs. {taxable_income:,.2f}")
    print(f"{'Tax Payable (Base)':<25} | Rs. {base_tax:,.2f}")
    for breakdown_item in tax_breakdown:
         print(f"  - {breakdown_item}")
    print(f"{'Health & Edu Cess (4%)':<25} | Rs. {cess:,.2f}")
    print(f"{'Total Tax Payable':<25} | Rs. {total_tax_payable:,.2f}")
    print("-" * 43)
    print(f"{'Annual Net Salary':<25} | Rs. {annual_net_salary:,.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
