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

    def __mul__(self, x):
        v = Vector(self.x, self.y, self.z)
        v.x *= x
        v.y *= x
        v.z *= x
        return v
