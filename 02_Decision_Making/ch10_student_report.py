def student_report_card():
    print("Coding Challenge 10: Student Report Card")
    try:
        name = input("Enter Student Name: ")
        score1 = float(input("Enter score for Subject 1: "))
        score2 = float(input("Enter score for Subject 2: "))
        score3 = float(input("Enter score for Subject 3: "))
        
        total = score1 + score2 + score3
        average = total / 3
        
        print("\n--- Report Card ---")
        print(f"Name: {name}")
        print(f"Total Score: {total}")
        print(f"Average Score: {average:.2f}")
        
        if average >= 60:
            print("Class: 1st Class")
        elif average >= 50:
            print("Class: 2nd Class")
        elif average >= 35:
            print("Class: Pass Class")
        else:
            print("Status: Fail")
            
    except ValueError:
        print("Invalid input! Please enter numeric scores.")

if __name__ == "__main__":
    student_report_card()
