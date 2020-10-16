class A:
    def process(self):
        print(type(self))
        print("Process in A")
        # self.doit()


class B:
    def process(self):
        print("Process in B")


class C(A, B):
    def task(self):
        # super().process()
        A.process(self)
        B.process(self)


obj_a = A()
obj_a.process()
obj_c = C()
obj_c.task()
