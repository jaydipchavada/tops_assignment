
subject_marks = int (input("Enter subject Marks:"))

if subject_marks>= 70 and subject_marks<=100:
    print("A grade")
elif subject_marks>=60:
    print("B grade")
elif subject_marks>=50:
    print("c grade")
elif subject_marks>=40:
    print("D grade")
elif subject_marks>=30:
    print("pass")
else:
    print("fail")

