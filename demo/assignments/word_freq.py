s = "How do you do? How did you do yesterday?"

words = set(s.split())
for w in words:
    print(f"{w} occurs {s.count(w)} times")
