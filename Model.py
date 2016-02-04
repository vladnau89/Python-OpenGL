from Vector import Vector

class Model:
    def __init__(self, file):
        self.file = file
        self.verts = []
        self.faces = []
        self.__load()

    def __load(self):
        f = open(self.file, "r")
        a = 0
        for line in f:
            split = line.split()
            if len(split) > 0:
                if split[0] == "v":
                    vector = Vector(float(split[1]), float(split[2]), float(split[3]))
                    self.verts.append(vector)
                elif split[0] == "f":
                    a += 1
                    face = Vector()
                    face.x = split[1].split("/")[0]
                    face.y = split[2].split("/")[0]
                    face.z = split[3].split("/")[0]
                    self.faces.append(face)

        print "verts = %s   faces = %s" % (len(self.verts), len(self.faces))
        f.close()
