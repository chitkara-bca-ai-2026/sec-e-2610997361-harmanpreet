num=float(input("enter a numerical value:"))
exp=float(input("enter an exponent :"))
decimal=float(input("enter a decimal measurement:"))
import math

ceil=math.ceil(decimal)
floor=math.floor(decimal)
print("----RESULT-----")
print("Value :", num)
print("Exponent:",exp)
print("Power(pow):",math.pow(num,exp))
print(f"Square Root(sqrt):{math.sqrt(num):.4f}")
print(f"Ceil Value:{ceil}")
print(f"Floor value:{floor}")
