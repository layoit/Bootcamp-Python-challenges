def series_squares_even():
    print("Coding Challenge 19: Display Series 4, 16, 36... N")
    try:
        n = int(input("Enter N (number of terms): "))
        print(*[(2*i)**2 for i in range(1, n+1)])
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    series_squares_even()
