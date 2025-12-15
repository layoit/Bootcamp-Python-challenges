def pattern_alt_squares():
    print("Coding Challenge 39: Pattern of Perfect Squares with Alternating Signs (N Rows)")
    try:
        n = int(input("Enter N: "))
        curr = 1
        for i in range(1, n+1):
            row_str = []
            for j in range(i):
                val = curr * curr
                if curr % 2 == 0:
                    val = -val
                row_str.append(val)
                curr += 1
            print(*row_str)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    pattern_alt_squares()
