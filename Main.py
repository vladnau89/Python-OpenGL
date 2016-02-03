from TGAImage import TGAImage, Format
from Color import Color


def main():
    image = TGAImage(100, 100, Format.RGBA)
    color_red = Color(255, 0, 0, 255)
    image.set(52, 41, color_red)
    image.write("output.tga")


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
