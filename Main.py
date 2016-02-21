from TGAImage import TGAImage, Format
from Color import Color
from Model import Model
from Vector import Vector
from random import randint
from math import fabs
import sys

red = Color(255, 0, 0, 255)
green = Color(0, 255, 0, 255)
blue = Color(0, 0, 255, 255)
white = Color(255, 255, 255, 255)

width = 700
height = 700

light_intensity_vector = Vector(0, 0, -0.7)


def main():

    image = TGAImage()
    image.read("obj/african_head_diffuse.tga")

    # model = Model("obj/african_head.obj")
    # image = TGAImage(width + 1, height + 1, Format.RGBA)
    #
    # # model.write("info.txt")
    # zbuffer = []
    #
    # for i in range(0, image.width * image.height):
    #     zbuffer.append(-sys.maxint - 1)
    #
    # for face in model.faces:
    #     screen_coord = [Vector(), Vector(), Vector()]
    #     world_coords = [Vector(), Vector(), Vector()]
    #     for i in range(0, 3):
    #         world_coord_vector = model.verts[int(face.get(i))]
    #         screen_coord[i].x = int((world_coord_vector.x + 1.) * width / 2)
    #         screen_coord[i].y = int((world_coord_vector.y + 1.) * height / 2)
    #         world_coords[i] = world_coord_vector
    #     n = (world_coords[2] - world_coords[0]) ^ (world_coords[1] - world_coords[0])
    #     norm = n.normalize()
    #     intensity = norm.mul(light_intensity_vector)
    #     if intensity < 0:  # skip invisible triangle
    #         continue
    #     # random_color = Color(randint(0, 255), randint(0, 255), randint(0, 255), 255)
    #     random_color = Color(int(intensity * 255), int(intensity * 255), int(intensity * 255), 255)
    #     triangle(screen_coord[0], screen_coord[1], screen_coord[2], image, random_color, zbuffer)
    #
    # image.write("output.tga")

    # scene = TGAImage(width + 1, height + 1, Format.RGBA)
    # line_by_vector(Vector(20, 34), Vector(644, 400), scene, red)
    # line_by_vector(Vector(120, 434), Vector(444, 400), scene, green)
    # line_by_vector(Vector(330, 463), Vector(594, 200), scene, blue)
    #
    # line_by_vector(Vector(10, 10), Vector(690, 10), scene, white)
    #
    # scene.write("scene.tga")
    #
    # render = TGAImage(width, 16, Format.RGBA)
    # buffer = []
    # for i in range(0, width):
    #     buffer.append(-sys.maxint - 1)
    #
    # rasterise(Vector(20, 34), Vector(644, 400), render, red, buffer)
    # rasterise(Vector(120, 434), Vector(444, 400), render, green, buffer)
    # rasterise(Vector(330, 463), Vector(594, 200), render, blue, buffer)
    #
    # render.write("render.tga")


def rasterise(point_vect0, point_vect1, image, color, ybuffer):
    p0 = point_vect0
    p1 = point_vect1

    if p0.x > p1.x:
        p0, p1 = p1, p0
    deltaX = float(p1.x - p0.x)
    for x in range(p0.x, p1.x, 1):
        t = (x - p0.x) / deltaX
        y = p0.y * (1 - t) + p1.y * t
        if ybuffer[x] < y:
            ybuffer[x] = y
            for i in range(0, image.height):
                image.set(x, i, color)


def triangle(v0, v1, v2, image, color, zbuffer):
    # line_by_vector(v1, v2, image, red)
    # line_by_vector(v1, v3, image, red)
    # line_by_vector(v2, v3, image, red)

    if v0.y > v1.y:
        v0, v1 = v1, v0
    if v0.y > v2.y:
        v0, v2 = v2, v0
    if v1.y > v2.y:
        v1, v2 = v2, v1

    total_height = int(v2.y - v0.y)

    for y in range(0, total_height):
        is_second_half = y >= v1.y - v0.y
        segment_height = v2.y - v1.y if is_second_half else v1.y - v0.y
        alpha = float(y) / total_height
        delta = (v1.y - v0.y) if is_second_half else 0
        beta = float(y - delta) / segment_height
        a = v0 + (v2 - v0) * alpha
        b = v1 + (v2 - v1) * beta if is_second_half else v0 + (v1 - v0) * beta

        if a.x > b.x:
            a, b = b, a

        for i in range(int(a.x), int(b.x)):
            phi = 1. if a.x == b.x else float((i - a.x)/ float(b.x - a.x))
            p = a + (b - a) * phi
            idx = int(p.x) + int(p.y * image.width)
            if zbuffer[idx] < p.z:
                zbuffer[idx] = p.z
                image.set(int(p.x), int(p.y), color)


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
