class Vector:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, str):
            try:
                x, y, z = eval(x)
            except Exception:
                raise ValueError()
        self.x = float(x)
        self.y = float(y) if y is not None else 0.0
        self.z = float(z) if z is not None else 0.0
        assert all(isinstance(i, (int, float)) for i in (self.x, self.y, self.z))

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        raise TypeError()

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


v1 = Vector("{1, 2, 3}")
v2 = Vector(4, 5, 6)

from itertools import combinations
def max_triangle_area(points):
    max_area = 0
    best_triangle = None
    for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
        area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
        if area > max_area:
            max_area = area
            best_triangle = ((x1, y1), (x2, y2), (x3, y3))
    return max_area, best_triangle
points = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2)]
max_area, triangle = max_triangle_area(points)
print(max_area)

