from TGAImage import TGAImage, Format
from Color import Color
from Model import Model
from Vector import Vector
from random import randint
from math import fabs

red = Color(255, 0, 0, 255)
green = Color(0, 255, 0, 255)
white = Color(255, 255, 255, 255)

width = 700
height = 700

light_intensity_vector = Vector(0, 0, -0.7)


def main():
    model = Model("obj/african_head.obj")
    image = TGAImage(width + 1, height + 1, Format.RGBA)

    # model.write("test.txt")

    for face in model.faces:
        screen_coord = [Vector(), Vector(), Vector()]
        world_coords = [Vector(), Vector(), Vector()]
        for i in range(0, 3):
            world_coord_vector = model.verts[int(face.get(i))]
            screen_coord[i].x = int((world_coord_vector.x + 1.) * width / 2)
            screen_coord[i].y = int((world_coord_vector.y + 1.) * height / 2)
            world_coords[i] = world_coord_vector
        n = (world_coords[2] - world_coords[0]) ^ (world_coords[1] - world_coords[0])
        norm = n.normalize()
        intensity = norm.mul(light_intensity_vector)
        if intensity < 0:   # skip invisible triangle
            continue

        # random_color = Color(randint(0, 255), randint(0, 255), randint(0, 255), 255)
        random_color = Color(int(intensity * 255), int(intensity * 255), int(intensity * 255), 255)
        triangle(screen_coord[0], screen_coord[1], screen_coord[2], image, random_color)
    # line(20, 13, 40, 80, image, red)
    # line(0, 0, width, height, image, red)
    # line(40, 80, 20, 13, image, red)
    #
    # t0 = [Vector(10, 70), Vector(50, 160), Vector(70, 80)]
    # t1 = [Vector(180, 50), Vector(150, 1), Vector(70, 180)]
    # t2 = [Vector(180, 150), Vector(120, 160), Vector(130, 180)]

    # triangle(t0[0], t0[1], t0[2], image, white)
    # triangle(t1[0], t1[1], t1[2], image, white)
    # triangle(t2[0], t2[1], t2[2], image, green)

    image.write("output.tga")


def triangle(v1, v2, v3, image, color):
    # line_by_vector(v1, v2, image, red)
    # line_by_vector(v1, v3, image, red)
    # line_by_vector(v2, v3, image, red)

    if v1.y > v2.y:
        v1, v2 = v2, v1

    if v1.y > v3.y:
        v1, v3 = v3, v1

    if v2.y > v3.y:
        v2, v3 = v3, v2

    total_height = int(v3.y - v1.y)

    for y in range(0, total_height, 1):
        is_second_half = y >= v2.y - v1.y
        segment_height = v3.y - v2.y if is_second_half else v2.y - v1.y
        alpha = float(y) / total_height
        delta = (v2.y - v1.y) if is_second_half else 0
        beta = float(y - delta) / segment_height
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
