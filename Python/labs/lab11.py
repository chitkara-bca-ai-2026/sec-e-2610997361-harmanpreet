user=input("Enter a username: ")
password=input("Enter a password: ")
length=len(password)>=8
has_digit=False
has_uppercase=False
for ch in password:
    if ch.isdigit():
        has_digit=True
    if ch.isupper():
        has_uppercase=True
print('')
print("=======================================")
print('       PASSWORD VALIDATION REPORT      ')
print('=======================================')
print("Username:",user)
print("Password:","*"*len(password))
print("------Validation Rules------")
if length:
    print("[PASS] Minimum 8 characters(10 characters)")
else:
    print("[FAIL] Minimum 8 characters(10 characters)")
if has_digit:
    print("[PASS] At Least one digit")
else:
    print("[FAIL] At Least one digit")
if has_uppercase:
    print("[PASS] At Least one uppercase letter")
else:
    print("[FAIL] At Least one uppercase letter")
print("---------Result----------")
if length and has_digit and has_uppercase:
    print("Password is VALID!")
    print(f"Account created successfully for {user}!")
else:
    print("Password is INVALID!")
print("=================================================")