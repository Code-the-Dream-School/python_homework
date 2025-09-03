import math

# Task 5: Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# Task 5: Vector class (inherits Point)
class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# --- Test code ---
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    print("Point 1:", p1)
    print("Point 2:", p2)
    print("Distance between points:", p1.distance_to(p2))

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print("Vector 1:", v1)
    print("Vector 2:", v2)
    print("Vector sum:", v3)
    print("v1 == v2?", v1 == v2)
    print("v3 == Vector(4, 6)?", v3 == Vector(4, 6))
