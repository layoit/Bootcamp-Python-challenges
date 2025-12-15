def pattern_star():
    print("Coding Challenge 34: Star Pattern (N Rows)")
    try:
        n = int(input("Enter N: "))
        for i in range(n):
            print("*****")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    pattern_star()
