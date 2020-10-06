
def zero(v):
    print(id(v))
    v = 0
    print(id(v))


n = 100
print(id(n))
zero(n)
print(id(n))
print(n)

