def generate_series_alt():
    print("Coding Challenge 42: Generate Series 1, -5, 9, -13 ... N")

    try:
        n = int(input("Enter N (number of terms): "))
        
        val = 1
        series = []
        for i in range(n):
            current_val = val
            if i % 2 != 0: # Odd index (1, 3, 5...) -> 2nd, 4th terms -> Negative
                current_val = -val
            
            series.append(current_val)
            val += 4
            
        print(*series)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    generate_series_alt()
