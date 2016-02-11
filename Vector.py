from math import sqrt

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def get(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y
        if i == 2:
            return self.z

    def __add__(self, other):
        v = Vector(self.x, self.y, self.z)
        v.x += other.x
        v.y += other.y
        v.z += other.z
        return v

    def __sub__(self, other):
        v = Vector(self.x, self.y, self.z)
        v.x -= other.x
        v.y -= other.y
        v.z -= other.z
        return v

    def __mul__(self, value):
        v = Vector(self.x, self.y, self.z)
        v.x *= value
        v.y *= value
        v.z *= value
        return v

    def __xor__(self, other):
        v = Vector(self.x, self.y, self.z)
        x = v.y * other.z - v.z * other.y
        y = v.z * other.x - v.x * other.z
        z = v.x * other.y - v.y * other.x
        return Vector(x, y, z)

    def normalize(self):
        v = Vector(self.x, self.y, self.z)
        length = 1. / sqrt(v.x * v.x + v.y * v.y + v.z * v.z)
        return v * length

    def mul(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

