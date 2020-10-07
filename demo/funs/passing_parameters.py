def zero(v):
    print(id(v))
    v = 0
    print(id(v))


def prepend(lst, value):
    lst.insert(0, value)


l = [1, 2, 3]
prepend(l, 10)
print(l)

n = 100
print(id(n))
zero(n)
print(id(n))
print(n)
