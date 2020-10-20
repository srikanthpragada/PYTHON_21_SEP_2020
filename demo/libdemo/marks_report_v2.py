f = open("marks.txt", "rt")
ef = open("errors.txt", "wt")

students = {}
for line in f:
    parts = line.split(",")
    if len(parts) < 2:
        ef.write(line + "\n")
        continue

    name = parts[0]
    marks = parts[1:]
    try:
        total = sum(map(int, marks))
        average = total / len(marks)
        students[name] = average  # add to dict
    except:
        ef.write(line + "\n")

f.close()
ef.close()

for (name, marks) in sorted(students.items()):
    print(f"{name:20} {marks:.2f}")
