
pwd = input("Enter password :")
upper = digit = special = False
special_chars = '@#_&*'

for ch in pwd:
    if ch.isupper():
        upper = True
    elif ch.isdigit():
        digit = True
    elif ch in special_chars:
        special = True


if upper and digit and special:
    print("Valid Password")
else:
    print("Invalid password")



