def pattern_12345():
    print("Coding Challenge 34 (Duplicate): Number Pattern 12345... (N Rows)")
    try:
        n = int(input("Enter N: "))
        for i in range(n):
            print("12345")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    pattern_12345()
