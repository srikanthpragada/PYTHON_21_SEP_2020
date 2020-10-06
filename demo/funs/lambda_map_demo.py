names = ['Abc', 'Pqr', 'Yye', 'Xyz']

for s in map(lambda v: v[:2], names):
    print(s)

marks = ['P60', 'J80', 'O77', 'C77']

print(sum(map(lambda s: int(s[1:]), marks)))
