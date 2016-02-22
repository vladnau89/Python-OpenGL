from Vector import Vector
from TGAImage import TGAImage

class Model:
    def __init__(self, file):
        self.file = file
        self.verts = []
        self.faces = []
        self.uv = []
        self.normals = []
        self.__diffusemap = TGAImage()
        self.__load()


    def __load(self):
        f = open(self.file, "r")
        for line in f:
            split = line.split()
            if len(split) > 0:
                if split[0] == "v":
                    vector = Vector(float(split[1]), float(split[2]), float(split[3]))
                    self.verts.append(vector)
                elif split[0] == "f":
                    face = [Vector(), Vector(), Vector()]
                    for i in range(0, 3):
                        face[i].x = int(split[i + 1].split("/")[0]) - 1    # 1 - based format
                        face[i].y = int(split[i + 1].split("/")[1]) - 1
                        face[i].z = int(split[i + 1].split("/")[2]) - 1
                    self.faces.append(face)
                elif split[0] == "vt":
                     texture = Vector(float(split[1]), float(split[2]), float(split[3]))
                     self.uv.append(texture)
                elif split[0] == "vn":
                     norm = Vector(float(split[1]), float(split[2]), float(split[3]))
                     self.normals.append(norm)
        print "%s    verts = %s   faces = %s   normals = %s   uv = %s" \
              % (self.file, len(self.verts), len(self.faces), len(self.normals), len(self.uv))
        f.close()
        self.__diffusemap.read(self.file.split(".")[0] + "_diffuse.tga")
        # self.__diffusemap.flip_vertically()
        # self.__diffusemap.write("nigga.tga")

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
        f.write('\n')
        for vt in self.vtextures:
            f.write('vt ' + str(vt.x) + '  ' + str(vt.y) + '  ' + str(vt.z) + '\n')
        f.write("textures = %s " % (len(self.vtextures)))
        f.close()

    def get_uv(self, iface, nvert):
        face = self.faces[iface]
        idx = face[nvert].get(1)
        return Vector(int(round(self.uv[idx].x * self.__diffusemap.width)), int(round(self.uv[idx].y * self.__diffusemap.height)))

    def get_norm(self, iface, nvert):
        face = self.faces[iface]
        idx = face[nvert].get(2)
        return self.normals[idx]

    def get_vert(self, iface, nvert):
        face = self.faces[iface]
        idx = face[nvert].get(0)
        return self.verts[idx]

    def diffuse(self, vect):
        return self.__diffusemap.get(int(round(vect.x)), int(round(vect.y)))

