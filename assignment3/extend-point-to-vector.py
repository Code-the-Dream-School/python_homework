class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Vector(Point):

    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
point1 = Point(3, 4)
point2 = Point(3, 4)
point3 = Point(0, 0)

print(point1)
print(point1 == point2)
print(point1.distance(point3))

vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

print(vector1)
print(vector1 + vector2)