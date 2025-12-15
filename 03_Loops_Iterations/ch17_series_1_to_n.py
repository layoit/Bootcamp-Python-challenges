def series_1_to_n():
    print("Coding Challenge 17: Display Series 1, 2, 3... N")
    try:
        n = int(input("Enter N: "))
        print(*[i for i in range(1, n+1)])
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    series_1_to_n()
