values = ["Mike,3939393", "Jack,83838383", "Ben,393939111", "Mike,4454598222",
          "Ben,399191121", "Joe,3939393311", "Robert,181818111","Steve"]

contacts = {}

for value in values:
    name, mobile = value.split(",")
    if name in contacts:
        contacts[name].add(mobile)  # add mobile to existing name
    else:
        contacts[name] = {mobile}  # new entry

for name, mobiles in sorted(contacts.items()):
    print(f"{name:20} {','.join(mobiles)}")
