# Function overloading

def add(a, b):
    pass

print(id(add))

add2 = add


def add(a, b, c):
    pass

print(id(add))
print(type(add))

add2(10, 20)
add(10, 20, 30)
