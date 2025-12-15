def series_fibonacci():
    print("Coding Challenge 24: Display Series 1, 1, 2, 3, 5, 8... N")
    try:
        n = int(input("Enter N (number of terms): "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        if n == 1:
            print(1)
        elif n == 2:
            print(1, 1)
        else:
            fib = [1, 1]
            for _ in range(n - 2):
                fib.append(fib[-1] + fib[-2])
            print(*fib)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    series_fibonacci()
