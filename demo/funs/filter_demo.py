def passed(marks):
    return marks >= 50


s = "How Do you DO"
for c in filter(str.isupper, s):
    print(c)

scores = [60, 45, 67, 88, 34]
for m in filter(passed, scores):
    print(m)

passed_marks = filter(passed, scores)
print(passed_marks)

passed_marks = list(filter(passed, scores))
print(passed_marks)
