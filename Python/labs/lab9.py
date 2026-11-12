a=int(input("Enter input:"))
print("pattern 1 : Star Triangle")
print('----------------------------')
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print() 

print("pattern 2 : Number Triangle")
print('----------------------------')
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("pattern 3 : Inverted Star Triangle")
print('----------------------------')
for i in range (a,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("pattern 4 : Pyramid")    
for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end="")
    for k in range((2*i)-1):
        print("*",end=" ")
    print()