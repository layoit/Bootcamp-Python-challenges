def series_squares_skip_4():
    print("Coding Challenge 21: Display Series 1, 4, 9, 25, 36, 49, 81... N")
    print("(Squares excluding multiples of 4)")
    try:
        n = int(input("Enter N (number of terms): "))
        series = []
        count = 0
        i = 1
        while count < n:
            if i % 4 != 0:
                series.append(i**2)
                count += 1
            i += 1
        print(*series)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    series_squares_skip_4()
