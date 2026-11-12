
t_fee=float(input("enter tuition fee:"))
lab_fee=float(input("enter lab fee:"))
e_fee=float(input("enter exam fee:"))
lia_fee=float(input("enter liabrary fee:"))
dis=float(input("enter discount amount:"))
sum = t_fee + e_fee + lia_fee + lab_fee
after_discount = sum - dis
a_fee = after_discount*2
mntly_cost = a_fee//12
print("\n------STUDENT FEE DETAILS-----")
print("Tuition Fee:",t_fee)
print("Lab Fee:",lab_fee)
print("Library Fee:",lia_fee)
print("Exam Fee:",e_fee)
print("Discount Fee:",dis)
print("Sum:",sum)
print("Fee after discount:",after_discount)
print("Annual Fee:",a_fee)
print("Montly Fee:",mntly_cost)