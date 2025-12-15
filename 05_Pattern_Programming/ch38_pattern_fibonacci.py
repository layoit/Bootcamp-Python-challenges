def pattern_fibonacci():
    print("Coding Challenge 38: Fibonacci Series Pattern (N Rows)")
    try:
        n = int(input("Enter N: "))
        
        # Calculate how many fib numbers we need: n*(n+1)/2
        total_nums = n * (n + 1) // 2
        
        fibs = [1, 1]
        while len(fibs) < total_nums:
            fibs.append(fibs[-1] + fibs[-2])
            
        idx = 0
        for i in range(1, n+1):
            row_vals = fibs[idx : idx + i]
            print(*row_vals)
            idx += i
            
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    pattern_fibonacci()
