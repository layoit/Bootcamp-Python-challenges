def number_to_words():
    print("Coding Challenge 41: Convert Number to Words (Mathematical Logic)")
    try:
        num = int(input("Enter a number: "))
        if num == 0:
            print("Zero")
            return
            
        digits_map = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
        }
        
        # Extract digits
        digits = []
        temp = abs(num)
        while temp > 0:
            digit = temp % 10
            digits.append(digit)
            temp = temp // 10
            
        # Digits are in reverse order logic wise (extracted from last)
        # So reverse simply or pop
        words = []
        if num < 0:
            words.append("Minus")
            
        for d in reversed(digits):
            words.append(digits_map[d])
            
        print("Output:", " ".join(words))
        
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    number_to_words()
