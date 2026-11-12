print('================================================')
print('            SCHOOL RESULTS PROCESSING           ')
print('================================================')
stud_name=input("Enter student name:")
roll_no=int(input("Enter roll number:"))
total=0
failed=False
for i in range(1,6):
    marks=int(input(f"enter marks for subject{i}: "))
    if marks<0 or marks>100:
        print("Invalid Marks! Enter marks between 0 and 100.")
        exit()
    total+=marks
    if marks<40:
        failed=True 
percentage=float((total/500)*100)
if failed :
    result="FAIL"
    grade="F"
    remark="Failed in one or more subjects"
elif percentage>=90:
    result="PASS"
    grade="A+"
    remark="outstanding"
elif percentage>=80:
    result="PASS"
    grade="A"
    remark="Excellent"
elif percentage>=70:
    result="PASS"
    grade="B"
    remark="Very Good"
elif percentage>=60:
    result="PASS"
    grade="C"
    remark="Good"
elif percentage>=50:
    result="PASS"
    grade="D"
    remark="satisfactory"
elif percentage>=40:
    result="PASS"
    grade="E"
    remark="Pass"
else:
    result="FAIL"
    grade="F"
    remark="Fail"
print('================================================')
print("          STUDENT REPORT CARD        ")
print('================================================')
print("Student Name:",stud_name)
print("Roll Number:",roll_no)
print('------------------------------------------------')
print("Total Marks :",f"{total:.1f}/ 500.0")
print("percentage :",f"{percentage:.1f}%")
print("Result :",result)
print("Grade :",grade)
print("Remark :",remark)
print('================================================')