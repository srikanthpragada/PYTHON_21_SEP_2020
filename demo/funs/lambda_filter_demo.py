s = "How Do you DO 123"
for c in filter(lambda c: c.islower() or c.isdigit(), s):
    print(c)

scores = [60, 45, 67, 88, 34]
for m in filter(lambda v: v >= 50, scores):
    print(m)
