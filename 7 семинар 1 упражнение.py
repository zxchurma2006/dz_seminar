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

print(v1)
print(v2)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 * 2)

print(abs(v1))
