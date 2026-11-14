students={
    "101":
    { "Name": "Aman" , 
     "Branch":"BCA AI" ,
     "Semester": "1", 
     "Marks":[85, 90,78]
     },
    "102":
      { "Name": "Riya",
        "Branch":"BCA AI",
        "Semester": "1", 
        "Marks":[92,88,95]
      },
    "103":
    { "Name": "Karan",
      "Branch": "BCA AI", 
      "Semester":"1", 
      "Marks":[74,80,82]
      }
}
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
        for roll , student  in students.items():
           print("Roll No:",roll , 
           "| Name:",student["Name"],
            "| Branch:", student["Branch"],
            "| Sem:",student["Semester"],
             "| Marks:",student["Marks"])
         
        print("Total Enrolled Students:",len(students))
    elif choice == 2:
        roll=input("Enter Roll Number to search:")
        student = students.get(roll)
        if student is not None:
            print("\n[FOUND] Record for Roll No",roll)
            print("Name     :", student["Name"])
            print("Branch   :", student["Branch"])
            print("Semester :", student["Semester"])
            print("Marks    :", student["Marks"])
        else:
            print("[ERROR] Student record not found.")
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

            print("[SUCCESS] student '",name,"' (roll no:",roll,
                     ") registered successfully.")
    elif choice== 4:
        roll=input("Enter Roll Number to update: ")
        if roll in students:
            student = students[roll]
            print("Current details for",
                  student["Name"], "(Roll",roll,"):")
            print("1. Branch:",student["Branch"] , 
              "|" , "2. Semester:",student["Semester"])
            field=int(input("Choose field to update (1 for Branch , 2 for Semester):"))
            if field ==1:
                new_branch= input("Enter new Branch:")
                student["Branch"] = new_branch
                print("[SUCCESS] Branch updated successfully.")
            elif field == 2:
                 new_semester=input("Enter new Semester:")
                 student["Semester"]  = new_semester
                 print(f"[SUCCESS] Semester updated to '{new_semester}'.")
            else:
                 print("[ERROR] Invalid field choice.")
        else:
              print("[ERROR]student record not found.")
    elif choice == 5:
        roll = (input("Enter Roll Number for Academic Performance:"))
        if roll in students:
            student = students[roll]
            marks = student["Marks"]
            total = sum(marks)
            average = total / len(marks)
            if average >=40:
                result = "PASS"
            else:
                result = "FAIL"
            print("======ACADEMIC REPORT======")
            print("Student Name :", student["Name"],
                 "(Roll No :",roll,")" )
            print("Subject Marks :", marks)
            print("Average Marks :", round(average,2), "%")
            print("Total Marks:",total,"/300")
            print("Final Result:", result)
            print("======================================================")
        else:
            print("[ERROR] Student record not found.")
    elif choice ==6:
        roll = input("Enter Roll Number to delete:")
        deleted_student = students.pop(roll, None) 
        if deleted_student is not None:
            print("[SUCCESS] Record for '",
                  deleted_student["Name"],
                  "'(Roll No:",roll,") deleted successfully.")
        else:
            print("[ERROR] Student record not found.")
    elif choice == 7:
        print("Thank you for using student Information Management System!")
        print("Goodbye!")
        break
    else:
        print("[ERROR] Invalid choice! please  select 1-7.")