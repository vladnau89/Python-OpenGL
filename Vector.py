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
