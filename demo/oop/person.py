class Person:
    def __init__(self, name, email):
        self.name = name
        self.__email = email  # private

    def display(self):
        print(self.name)
        print(self.__email)


p = Person("Srikanth", "srikanthpragada@gmail.com")
# p._Person__email = "contact@srikanthtechnologies.com"
p.mobile = "3939393333"
print(p.__dict__)
p.display()

p2 = Person("Abc",'abc@gmail.com')
print(p2.__dict__)