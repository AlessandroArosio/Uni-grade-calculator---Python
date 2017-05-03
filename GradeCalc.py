cw1 = None
cw2 = None
cw3 = None
grade1 = None
grade2 = None
grade3 = None
total = None
weight = None
second = False
third = False
print("Input first grade and its weight in percentage")
cw1 = float(input("Grade: "))
weight = int(input("Weight: "))
grade1 = cw1*(weight/100)
total = grade1
print()
second = input("There is another grade to calculate? y/n\n")
if second == "y":
    print("Input second grade and its weight in percentage")
    cw2 = float(input("Grade: "))
    weight = int(input("Weight: "))
    grade2 = cw2*(weight/100)
    total = total + grade2
third = input("There is another grade to calculate? y/n\n")
if third == "y":
    print("Input third grade and its weight in percentage")
    cw3 = float(input("Grade: "))
    weight = int(input("Weight: "))
    grade3 = cw3*(weight/100)
    total = total + grade3
if third == "y":
    print("\nYour total score is: %.2f " % total)
    print("The weighted first grade is %.2f " % grade1)
    print("The weighted second grade is %.2f " % grade2)
    print("The weighted third grade is %.2f " % grade3)
elif second == "y":
    print("\nYour total score is: %.2f " % total)
    print("The weighted first grade is %.2f " % grade1)
    print("The weighted second grade is %.2f " % grade2)
else:
    print("\nYour total score is: %.2f " % total)
if third == "y" and total >= 40:
    print("Exam PASSED!")
elif third == "y" and total <40:
    print("Exam FAILED!")
