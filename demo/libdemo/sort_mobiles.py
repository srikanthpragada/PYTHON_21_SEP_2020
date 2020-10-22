import re

mobiles = set()

f = open("mobiles.txt", "rt")

for line in f:
    numbers = re.findall(r'\d+', line)
    for n in numbers:
        if len(n) == 10:
            mobiles.add(n)

for n in sorted(mobiles):
    print(n)
