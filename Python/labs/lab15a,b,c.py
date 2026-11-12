students=[
    ("Roll No: 101", "Name: Aman" , "Branch:BCA AI" , "Semester: 1", "Marks:[85, 90,78]")
    ("Roll No: 102", "Name: Riya", "Branch:BCA AI", "Semester: 1", "Marks:[92,88,95]")
    ("Roll No:103", "Name: Karan", "Branch: BCA AI", "Semester:1", "Marks:[74,80,82]")
]
print("============================================================")
print("            STUDENT INFORMATION MANAGEMENT SYSTEM           ")
print("============================================================")
while True:
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    choice=int(input("Enter your choice(1-7):"))
    if choice == 1:
        print("---Enrolled Student Records---")
        for roll , student  in student.item():
           print("Roll No:",roll , 
           "|Name:",student["Name"],
            "|Branch:", student["Branch"],
            "|Sem:",student["Semester"],
             "|Marks:",student["Marks"])
         
        print("Total Enrolled Students:",len(students))
    elif choice == 2:
        roll=(input("Enter Roll Number to search:"))
        student=students.get(roll)
        if student is not None:
            print("[FOUND] Record for Roll No",roll)
            print("Name     :", student["Name"])
            print("Branch   :", student["Branch"])
            print("Semester :", student["Semester"])
            print("Marks    :", student["Marks"])
        else:
            print("[ERROR] Student record not found")
    elif choice == 3:
        print("---Register New Student---")
        roll=input("Enter Roll Number:")
        if roll in students:    
            print("[ERROR] Roll Number already exits.")
        else:
            name= input("Enter student Name:")
            branch=input("Enter Branch (e.g. BCA AI):")
            semester=input("Enter Semester:")
            marks=[]
            print("Enter marks obtained in 3 subjects:")

            for i in range(3):
                mark=int(input("Subject" + str(i+1) + ":"))
                marks.append(mark)
                students[roll]={
                    "Name": name,
                    "Branch": branch,
                    "Semester": semester,
                    "Marks": marks
                }
                print("[SUCCESS] student",name,
                      "registered successfully.")
    elif choice== 4:
        roll=input("Enter Roll Number to update: ")
        if roll in students:
            student = students[roll]
            print("Current details for",
                  student["Name"], "(Roll",roll,")")
            