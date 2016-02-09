from TGAImage import TGAImage, Format
from Color import Color
from Model import Model

red = Color(255, 0, 0, 255)
white = Color(255, 255, 255, 255)

width = 700
height = 700

def main():
    model = Model("obj/african_head.obj")
    image = TGAImage(width + 1, height + 1, Format.RGBA)

    model.write("test.txt")

    for face in model.faces:
        for i in range(0, 3):
            v0 = model.verts[int(face.get(i))]
            v1 = model.verts[int(face.get((i + 1) % 3))]
            x0 = (v0.x + 1.) * width / 2.
            y0 = (v0.y + 1.) * height/2.
            x1 = (v1.x + 1.) * width/2.
            y1 = (v1.y + 1.) * height/2.
            line(int(x0), int(y0), int(x1), int(y1), image, white)

    #line(20, 13, 40, 80, image, red)
    #line(0, 0, width, height, image, red)
    #line(40, 80, 20, 13, image, red)
    image.write("output.tga")


def line(x0, y0, x1, y1, image, color):
    steep = None
    if abs(x1 - x0) < abs(y1 - y0):
        y0, x0 = x0, y0
        y1, x1 = x1, y1
        steep = True

    x0, x1 = swap_if_bigger(x0, x1)
    y0, y1 = swap_if_bigger(y0, y1)
    for x in range(x0, x1, 1):
        t = (x - x0) / float(x1 - x0)
        y = y0*(1 - t) + y1*t
        if steep:
            image.set(int(y), int(x), color)
        else:
            image.set(int(x), int(y), color)


def swap_if_bigger(s1, s2):
    if s2 < s1:
        return s2, s1
    else:
        return s1, s2

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
