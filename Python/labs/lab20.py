import os
def append_entry(filename,entry):
    with open(filename , "a") as file:
        file.write(entry + '\n')
    print("[SUCCESS] New entry logged to", filename,
          ".")   
def display_log(filename):
    print("===========DAILY LOG BOOK===========")
    with open(filename,"r") as f:
        entries =  f.readlines()
    if len(entries) == 0:
        print("No log entries found.")
    else:
       for i, entry in enumerate(entries , start=1):
           print(f"[{ i:02d}] {entry.strip()}") 
    print("Total Logged Entries:", len(entries))
    print("=============================================")
filename="daily_log.txt"
if  os.path.exists(filename): 
   with open(filename , "w") as file:
    
        file.write(" 09:00 AM - System server startup verified.\n")
        file.write(" 10:30 AM - Morning attendance synchronized.\n")
        file.write(" 02:15 PM - Network security patch applied.")
print("=============================================================")
print("                      OFFICE DAILY LOG BOOK                  ")
print("=============================================================")
while True:
    print("Select an operation:")
    print("1. Add Log Entry ")
    print("2. Display Complete Log")
    print("3. Exit")
    choice= input("Enter choice(1-3):")
    if choice == "1":
        entry = input("Enter log entry:")
        append_entry(filename,entry)
    elif choice =="2":
        display_log(filename)
    elif choice == "3":
        print("Thank you for using the Daily Log Book . Goodbye!")
        break
    else:
        print("[ERROR] Invalid choice! Please select 1-3.")