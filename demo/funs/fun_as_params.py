def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def operation(a, b, fun):
    print(fun(a, b))


operation(10, 20, add)
operation(10, 20, mul)
# operation(10, 20, len)
