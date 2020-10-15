class A:
    def process(self):
        print("Process in A")


class B(A):
    def process(self):
        print("Process in B")


class C(A, B):
    pass


obj = C()
obj.process()
