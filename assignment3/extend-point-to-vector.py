import math


# Task 5: Extending a Class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    def __str__(self):
        return f"Vector < {self.x}, {self.y} >"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(4, 6)
p3 = Point(1, 2)
print(p1, p2)
print("p1 == p2:", p1 == p2)
print("p1 == p3:", p1 == p3)
print("distance p1 to p2:", p1.distance(p2))

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1, v2)
print("v1 == v2:", v1 == v2)
print("v1 + v2 =", v1 + v2)
print("distance v1 to v2:", v1.distance(v2))
