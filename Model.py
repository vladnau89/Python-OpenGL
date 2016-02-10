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
                    face.x = int(split[1].split("/")[0]) - 1    # 1 - based format
                    face.y = int(split[2].split("/")[0]) - 1
                    face.z = int(split[3].split("/")[0]) - 1
                    self.faces.append(face)

        print "verts = %s   faces = %s" % (len(self.verts), len(self.faces))
        f.close()

    def write(self, filename):
        f = open(filename, "w")
        for v in self.verts:
            f.write('v ' + str(v.x) + '  ' + str(v.y) + '  ' + str(v.z) + '\n')
        f.write('\n')
        f.write("verts = %s " % (len(self.verts)))
        f.write('\n')
        for ff in self.faces:
            f.write('f ' + str(ff.x) + '  ' + str(ff.y) + '  ' + str(ff.z) + '\n')
        f.write("faces = %s " % (len(self.faces)))
        f.close()
