#!/usr/bin/python -tt
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

        f.write(struct.pack("b", 0))  # id length
        f.write(struct.pack("b", 0))  # color map type
        f.write(struct.pack("b", 2))  # data type code. true color.uncompressed

        f.write(struct.pack("h", 0))  # color map origin
        f.write(struct.pack("h", 0))  # color map length
        f.write(struct.pack("b", 0))  # color map depth

        f.write(struct.pack("h", 0))  # x_origin
        f.write(struct.pack("h", 0))  # y_origin
        f.write(struct.pack("h", self.width))  # x_origin
        f.write(struct.pack("h", self.height))  # x_origin

        f.write(struct.pack("b", self.format << 3))  # bits per pixel
        f.write(struct.pack("b", 1 << 4))  # image descriptor. from left to right

        f.write(self.__data)
        f.close()
        print "saved"

    def set(self, x, y, color):
        if (x < 0 or x >= self.width) or (y < 0 or y >= self.height):
            print 'bad value'
            return

        index = (x + y * self.width) * self.format
        self.__data[index + 0] = color.b()
        self.__data[index + 1] = color.g()
        self.__data[index + 2] = color.r()
        self.__data[index + 3] = color.a()
