f = open("marks.txt", "rt")

for line in f:
    parts = line.split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    marks = parts[1:]
    try:
       total = sum(map(int, marks))
       average = total / len(marks)
       print(f"{name:20} {average:.2f}")
    except:
        pass

f.close()
