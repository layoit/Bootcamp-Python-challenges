def series_odds():
    print("Coding Challenge 18: Display Series 1, 3, 5... N")
    try:
        n = int(input("Enter N: "))
        print(*[i for i in range(1, n+1, 2)])
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    series_odds()
