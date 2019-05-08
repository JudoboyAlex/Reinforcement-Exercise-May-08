print("Enter your grade in percentage")
mark = int(input())

def grade_report(mark):
    
    if mark >= 90:
        print("A+")
    elif mark >= 80 and mark < 90:
        print("A")
    elif mark >=75 and mark < 80:
        print("B+")
    elif mark >= 70 and mark < 75:
        print("B")
    elif mark >= 65 and mark < 70:
        print("C+")
    elif mark >= 60 and mark < 65:
        print("C")
    elif mark >= 55 and mark < 60:
        print("D+")
    elif mark >= 50 and mark < 55:
        print("D")
    else:
        print("F")

grade_report(mark)