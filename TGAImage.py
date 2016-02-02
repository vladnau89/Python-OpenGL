#!/usr/bin/python -tt

import sys
import struct


class Format:
    GRAYSCALE = 1
    RGB = 3
    RGBA = 4


class TGAImage:
    def __init__(self, width, height, format):
        self.width = width
        self.height = height
        self.format = format
        self.__data = bytearray(width * height * format)

    def write(self, filename):
        f = open(filename, "wb")

        f.write(struct.pack("b", 0))  # idlength
        f.write(struct.pack("b", 0))  # colormaptype
        f.write(struct.pack("b", 2))  # datatypecode

        f.write(struct.pack("h", 0))  # colormaporigin
        f.write(struct.pack("h", 0))  # colormaplength
        f.write(struct.pack("b", 0))  # colormapdepth

        f.write(struct.pack("h", 0))  # x_origin
        f.write(struct.pack("h", 0))  # y_origin
        f.write(struct.pack("h", self.width))  # x_origin
        f.write(struct.pack("h", self.height))  # x_origin

        f.write(struct.pack("b", self.format))  # bitsperpixel
        f.write(struct.pack("b", 0x20))  # imagedescriptor

        f.write(self.__data)
        f.close()
        print "saved"


def main():
    image = TGAImage(100, 100, Format.RGBA)
    image.write("output.tga")


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
