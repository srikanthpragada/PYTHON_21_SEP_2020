names = []

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    names.append(name)

with open("names.txt", "wt") as f:
    for name in sorted(names):
        f.write(name + "\n")
