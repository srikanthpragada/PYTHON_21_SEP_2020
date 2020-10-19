def digits(st):
    for ch in st:
        if ch.isdigit():
            yield ch


g = digits("Python 3.9.0")
print(type(g))

# for d in g:
#     print(d)

print(next(g))
print("Now second one...")
print(next(g))