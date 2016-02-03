from TGAImage import TGAImage, Format
from Color import Color


def main():
    color_red = Color(255, 0, 0, 255)
    color_white = Color(255, 255, 255, 255)

    image = TGAImage(100, 100, Format.RGBA)

    #line(20, 13, 40, 80, image, color_white)
    line(40, 80, 20, 13, image, color_red)

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
