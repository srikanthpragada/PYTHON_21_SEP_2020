evens = []
odds = []

while True:
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

for v in evens + odds:
    print(v)
