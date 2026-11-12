
books=[
    ("Python Crash Course" , "Eric Matthes" , "2019" , "Programming"),
    ("Automate the Boring Stuff" , "Al Sweigart" , "2020" , "Programming"),
    ("Artificial Intelligence: A Modern Approach" , "Stuart Russell" , "2021" , "AI"),
    ("Clean Code ", "Robert C. Martin " , "2008" , "Software Engineering")
]
library_categories=set()
for book in books:
    library_categories.add(book[3])
student_wishlist={"AI","Cloud Computing" , "Robotics" ,"Cybersecurity"}
print("==================================================")
print("          LIBRARY BOOK & CATEGORY MANAGER         ")
print("==================================================")
while True:
   
    print("Select an operation:")
    print("1. View  Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
  
    choice=int(input("Enter your choice(1-6):"))
    
    if choice == 1:
        print("----Current Library Catalog (Fixed Records)----")
        for i , book in enumerate(books, start=1):
            title, author, year, category = book
            print(f'{i}.  "{title}" by {author}({year})| Genre:{category}')

        print("Total Books:", len(books))

    elif choice==2:
        print("----Add New Book Record----")
        title=input("Enter book title:")
        author=input("Enter book author:")
        year=input("Enter published year:")
        category=input("Enter category/ genre:")
        new_book = ( title, author , year , category)
        books.append(new_book)
        library_categories.add(category)
        print(f'[SUCCESS] "{title} added as an immutable catalog record.')
        print(f'[info] Category set updated with :"{category}"')

    elif choice==3:
        print("----Unique Categories Available in Library (Set)----")
        for category in sorted(library_categories):
            print("-",category)
        print("Total Unique Genres:",len(library_categories))

    elif choice==4:
        print("----Add to Student Wishlist----")
        category=input("Enter requested category:")
        student_wishlist.add(category)
        print(f'[SUCCESS] "{category}" added to student wishlist')

    elif choice==5:
        print("==================CATEGORY GAP ANALYSIS====================")
        print("Library Holdings(Set):",sorted(library_categories))
    
        print("Student Wishlist (Set):",sorted(student_wishlist))

        common = library_categories.intersection(student_wishlist)
        missing = student_wishlist.difference(library_categories)
        combined=library_categories.union(student_wishlist)
        print('-------------------------------------------------------------------------------------')
        print("1. Already in Stock (Intersection &):")
        print(sorted(common))
        print("2. Purchase Order Needed (Difference -):")
        print(sorted(missing))
        print("3. Full Combined Genre Coverage (Union |): ")
        print(sorted(combined))
        print('=======================================================================================')
    elif choice==6:
        print("Thank you for using the Library Manager . Goodbye!")
   
        break
    else:
        print("Invalid choice ! Please enter between 1 and 6 .")