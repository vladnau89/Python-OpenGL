from TGAImage import TGAImage, Format
from Color import Color
from Model import Model
from Vector import Vector

red = Color(255, 0, 0, 255)
green = Color(0, 255, 0, 255)
white = Color(255, 255, 255, 255)

width = 400
height = 400

def main():
    # model = Model("obj/african_head.obj")
    image = TGAImage(width + 1, height + 1, Format.RGBA)

    #model.write("test.txt")

    # for face in model.faces:
    #     for i in range(0, 3):
    #         v0 = model.verts[int(face.get(i))]
    #         v1 = model.verts[int(face.get((i + 1) % 3))]
    #         x0 = (v0.x + 1.) * width / 2.
    #         y0 = (v0.y + 1.) * height/2.
    #         x1 = (v1.x + 1.) * width/2.
    #         y1 = (v1.y + 1.) * height/2.
    #         line(int(x0), int(y0), int(x1), int(y1), image, white)

    #line(20, 13, 40, 80, image, red)
    #line(0, 0, width, height, image, red)
    #line(40, 80, 20, 13, image, red)

    t0 = [Vector(10, 70), Vector(50, 160), Vector(70, 80)]
    t1 = [Vector(180, 50), Vector(150, 1), Vector(70, 180)]
    t2 = [Vector(180, 150), Vector(120, 160), Vector(130, 180)]

    triangle(t0[0], t0[1], t0[2], image, white)
    # triangle(t1[0], t1[1], t1[2], image, white)
    # triangle(t2[0], t2[1], t2[2], image, green)

    image.write("output.tga")


def triangle(v1, v2, v3, image, color):
    line_by_vector(v1, v2, image, color)
    line_by_vector(v1, v3, image, color)
    line_by_vector(v2, v3, image, color)

    if v1.y > v2.y:
        v1, v2 = v2, v1

    if v2.y > v3.y:
        v2, v3 = v3, v2

    if v1.y > v3.y:
        v1, v3 = v3, v1

    total_height = v3.y - v1.y

    for y in range(0, total_height, 1):
        is_second_half = y >= v2.y - v1.y
        segment_height = v3.y - v2.y if is_second_half else v2.y - v1.y
        alpha = float(y) / total_height
        delta = (v2.y - v1.y) if is_second_half else 0
        beta  = float(y - delta) / segment_height
        a = v1 + (v3 - v1) * alpha
        b = v2 + (v3 - v2) * beta if is_second_half else v1 + (v2 - v1) * beta

        if a.x > b.x:
            a, b = b, a

        for i in range(int(a.x), int(b.x), 1):
            image.set(i, v1.y + y, color)


def line_by_vector(v1, v2, image, color):
    line(v1.x, v1.y, v2.x, v2.y, image, color)


def line(x0, y0, x1, y1, image, color):
    steep = None
    if abs(x1 - x0) < abs(y1 - y0):
        y0, x0 = x0, y0
        y1, x1 = x1, y1
        steep = True

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    for x in range(x0, x1, 1):
        t = (x - x0) / float(x1 - x0)
        y = y0 * (1 - t) + y1 * t
        if steep:
            image.set(int(y), int(x), color)
        else:
            image.set(int(x), int(y), color)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
