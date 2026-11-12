inventory=["Notebook","Pen","Eraser","Ruler"]
print('=================================================')
print('           INVENTORY CONTROL SYSTEM              ')
print('=================================================')

while True:
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    choice=int(input("Enter your choice(1-5):"))
    if choice==1:
        print("----Current Inventory----")
        for i , item in enumerate(inventory, start=1):
            print(f"{i}. {item}")
    elif choice==2:
        item=input("Enter item name to add:")
        if item:
            inventory.append(item)
            print(f"[SUCCESS]'{item}' added to inventory.")
        else:
            print("[ERROR] Item name cannot be empty.")

    elif choice==3:
        item=input("Enter item name to remove:")
        if item in inventory :
            inventory.remove(item)
            print(f"[SUCCESS] '{item}' removed from inventory.")
        else:
            print("[ERROR] Item not found in inventory.")

    elif choice==4:
        inventory.sort(key=str.lower)
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for i , item in enumerate(inventory , 1):
            print(f"{i}. {item}")

    elif choice==5:
        print("Thank you for using Inventory Control System!")
        break
    else:
        print("[ERROR] Invalid choice! Please enter 1 to 5.")