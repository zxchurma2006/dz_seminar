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
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
def center_of_mass(points):
    total_vector = Vector(0, 0)
    num_points = len(points)
    for point in points:
        total_vector += point
    return total_vector / num_points
points = [Vector(1, 2), Vector(3, 4), Vector(5, 6)]
com = center_of_mass(points)
print(com)
