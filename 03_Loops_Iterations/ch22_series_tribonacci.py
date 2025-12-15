def series_tribonacci_like():
    print("Coding Challenge 22: Display Series 1, 4, 7, 12, 23... N")
    print("(Sum of previous 3 terms)")
    try:
        n = int(input("Enter N (number of terms): "))
        if n == 1:
            print(1)
            return
        elif n == 2:
            print(1, 4)
            return
        elif n == 3:
            print(1, 4, 7)
            return
            
        series = [1, 4, 7]
        for _ in range(n - 3):
            next_val = sum(series[-3:])
            series.append(next_val)
        print(*series)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    series_tribonacci_like()
