
class Person:
    def __init__(self,name, email):
        self.name = name
        self.__email = email  # private

    def display(self):
        print(self.name)
        print(self.__email)


p = Person("Srikanth", "srikanthpragada@gmail.com")
p.__email = "contact@srikanthtechnologies.com"
print(p.__dict__)
p.display()