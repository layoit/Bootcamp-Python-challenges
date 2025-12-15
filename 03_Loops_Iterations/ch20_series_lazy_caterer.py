def series_lazy_caterer():
    print("Coding Challenge 20: Display Series 1, 2, 4, 7, 11... N")
    try:
        n = int(input("Enter N (number of terms): "))
        series = [1]
        for i in range(1, n):
            series.append(series[-1] + i)
        print(*series)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    series_lazy_caterer()
