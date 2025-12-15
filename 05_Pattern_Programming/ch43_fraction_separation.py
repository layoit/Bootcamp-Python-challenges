import math

def separate_whole_fraction():
    print("Coding Challenge 43: Whole and Fraction Separation")
    try:
        val = float(input("Enter a double value: "))
        
        whole = int(val)
        fraction = val - whole
        
        # Handling potential float precision issues for display
        print(f"Original: {val}")
        print(f"Whole Part: {whole}")
        print(f"Fractional Part: {fraction}") 
        # Note: 12.34 might show fraction as 0.3400000000000016 due to float representation.
        # This is expected behavior for floats.
        
    except ValueError:
        print("Invalid input! Please enter a decimal number.")

if __name__ == "__main__":
    separate_whole_fraction()
