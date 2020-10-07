g = 100  # Global variable


def fun1():
    a = 10  # Enclosing variable
    global g
    g = 1

    # Local function
    def fun2():
        nonlocal a
        a = a + 1
        b = 20  # Local variable
        print("In fun2()")
        print("Local function ", a, b, g)

    print("In fun1()")
    fun2()
    print("Enclosing function ", a)



fun1()
print(g)
