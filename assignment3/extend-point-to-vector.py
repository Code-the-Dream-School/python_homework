import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    print(p1 == p2)
    print(str(p1))
    print(p1.distance(p2))

    v1 = Vector(3, 4)
    v2 = Vector(1, 1)
    v3 = v1 + v2
    print(v3)
