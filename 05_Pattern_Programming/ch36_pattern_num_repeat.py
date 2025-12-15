def pattern_num_repeat():
    print("Coding Challenge 36: Number Increasing Pattern (1, 22, 333...) (N Rows)")
    try:
        n = int(input("Enter N: "))
        for i in range(1, n+1):
            print(str(i) * i)
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    pattern_num_repeat()
