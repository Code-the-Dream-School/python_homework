#Task 5a. Class Extension
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Checks if two points are equal
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __repr__(self):
        # String representation for debugging
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        # User-friendly string representation
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        # Calculates Euclidean distance to another point
        if not isinstance(other, Point):
            raise ValueError("Argument must be a Point")
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)

# Demo of all features
if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    p3 = Point(1, 2)
    print("Equality:", p1 == p2)  # True
    print("String representation (Point):", str(p1))  # (3, 4)
    print("Distance:", p1.distance_to(p3))  # Should be sqrt(8)

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print("String representation (Vector):", str(v1))  # Vector<1, 2>
    v3 = v1 + v2
    print("Vector addition:", v3)  # Vector<4, 6>