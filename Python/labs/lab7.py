print('===============================================')
print('          CALENDAR VERIFICATION SYSTEM         ')
print('===============================================')
year=int(input("Enter year:"))
if year<=0:
    print("Error: Please enter a  positive year.")
else:
    if year%400==0:
        status="LEAP YEAR"
        reason="Century year divisible by 400"
    elif year%100==0:
        status="COMMON YEAR"
        reason="Century tear divisible by 400"
    elif year%4==0:
        status="LEAP YEAR"
        reason="Divisible by 4 and not a century year"
    else:
        status="COMMON YEAR"
        reason="Not divisible by 4"
    if status=="LEAP YEAR":
        february_days=29
        total_days=366
    else:
        february_days=28
        total_days=365

    print('=============================================')
    print("Year:",year)
    print("Status:",status)
    print("Days in year:",total_days,"days")
    print("Days in February:",february_days,"days")
    print("Reason:",reason)
    print('============================================')