contacts = {}

while True:
    contact = input("Enter contact [end to stop] :")
    if contact == "end":
        break
    name, mobile = contact.split(",")
    contacts[name] = mobile

for name, mobile in sorted(contacts.items()):
    print(f"{name:20} {mobile}")
