import math

def pattern_factorials():
    print("Coding Challenge 40: Pattern of Factorials (N Rows)")
    try:
        n = int(input("Enter N: "))
        curr_fact_idx = 1
        for i in range(1, n+1):
            row_vals = []
            for j in range(i):
                row_vals.append(math.factorial(curr_fact_idx))
                curr_fact_idx += 1
            print(*row_vals)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    pattern_factorials()
