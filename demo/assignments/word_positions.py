s = "How do you do? How did you do yesterday?"
w = "do"

pos = -1
while True:
    pos = s.find(w, pos + 1)
    if pos == -1:
        break

    print(pos)
