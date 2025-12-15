def pattern_11111():
    print("Coding Challenge 33 (Duplicate): Number Pattern 11111... (N Rows)")
    try:
        n = int(input("Enter N: "))
        for i in range(1, n+1):
            print(str(i) * 5)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    pattern_11111()
