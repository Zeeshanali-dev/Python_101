student_score = int(input("Enter your score: "))

if student_score >=100:
    print("Enter Valid Number between 0-100")
elif student_score >=90:
    print("A")
elif student_score >=80:
    print("B")
elif student_score >=70:
    print("C")
elif student_score >=60:
    print("D")
else:
    print("F")