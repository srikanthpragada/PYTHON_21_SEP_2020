class Student:
    courses = {'java': 8000, 'python': 10000, 'ds': 20000}

    @staticmethod
    def changefee(course, newfee):
        Student.courses[course] = newfee

    def __init__(self, name, course, feepaid=0):
        self.name = name
        if course not in Student.courses:
            raise ValueError('Invalid course!')
        self.course = course
        self.feepaid = 0

    def pay(self, amount):
        self.feepaid += amount

    def getdue(self):
        return Student.courses[self.course] - self.feepaid


Student.changefee('python', 15000)
s = Student('Larry', 'python 3')
s.pay(5000)
print(s.getdue())
