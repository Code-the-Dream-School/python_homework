import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("Can only calculate distance between Points")
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Vector(Point):
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vectors to Vectors")
        return Vector(self.x + other.x, self.y + other.y)

if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(6, 8)
    p3 = Point(3, 4)

    print(f"Points: {p1}, {p2}, {p3}")
    print(f"p1 == p2: {p1 == p2}")
    print(f"p1 == p3: {p1 == p3}")
    print(f"Distance between p1 and p2: {p1.distance_to(p2):.2f}")

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print(f"\nVectors: {v1}, {v2}")
    print(f"Vector addition: {v1 + v2}")

    try:
        print(p1 + v1)
    except TypeError as e:
        print(f"\nError when adding Point and Vector: {e}")

    print(f"Distance between p1 and v1: {p1.distance_to(v1):.2f}")