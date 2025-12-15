def series_plus_4_skip_5():
    print("Coding Challenge 23: Display Series 1, 5, 9, 13... N")
    print("(+4 sequence skipping every 5th term)")
    try:
        n = int(input("Enter N (number of terms): "))
        series = []
        count = 0
        val = 1
        term_idx = 1
        while count < n:
            if term_idx % 5 != 0:
                series.append(val)
                count += 1
            val += 4
            term_idx += 1
        print(*series)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    series_plus_4_skip_5()
