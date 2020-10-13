class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x < other.x:
            return False

        if self.y > other.y:
            return True
        else:
            return False

    # p1 + p2
    # p1 + int
    def __add__(self, other):
        if isinstance(other, int):
            return Point(self.x + other, self.y + other)
        else:
            return Point(self.x + other.x, self.y + other.y)

    def __int__(self):
        return self.x + self.y


p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(11, 30)

print(p1 == p2)  # p1.__eq__(p2)
print(p1)  # p1.__str__()
print(p3 > p2)  # p2.__gt__(p3)

points = [Point(10, 20), Point(20, 10), Point(5, 5)]

for p in sorted(points):
    print(p)

for p in sorted(points, key=lambda v: v.y):
    print(p)

print(p1 + p2)   # p1.__add__(p2)
print(p1 + 10)   # p1.__add__(10)
print(int(p1))   # p1.__int__(p1)
