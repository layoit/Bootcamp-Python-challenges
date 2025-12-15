def pattern_num_sequence():
    print("Coding Challenge 37: Number Increasing Pattern (1, 12, 123...) (N Rows)")
    try:
        n = int(input("Enter N: "))
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end="")
            print()
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    pattern_num_sequence()
