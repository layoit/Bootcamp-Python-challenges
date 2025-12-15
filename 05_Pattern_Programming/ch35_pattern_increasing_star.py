def pattern_increasing_star():
    print("Coding Challenge 35: Increasing Star Pattern (N Rows)")
    try:
        n = int(input("Enter N: "))
        for i in range(1, n+1):
            print("*" * i)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    pattern_increasing_star()
