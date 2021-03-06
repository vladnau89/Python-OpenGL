#!/usr/bin/python -tt
import struct
from Color import Color
import Vector

class Format:
    GRAYSCALE = 1
    RGB = 3
    RGBA = 4


class TGAImage:
    def __init__(self, width=0, height=0, format=Format.RGBA):
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
        f.write(struct.pack("h", self.width))  # width
        f.write(struct.pack("h", self.height))  # height

        f.write(struct.pack("b", self.format << 3))  # bits per pixel
        f.write(struct.pack("b", 1 << 4))  # image descriptor. from left to right

        f.write(self.__data)
        f.close()
        print "%s   saved" % filename


    def read(self, filename):
        f = open(filename, "rb")
        f.read(1)   # id length
        f.read(1)   # color map type
        datatype = struct.unpack("b", f.read(1))[0]   # data type code

        f.read(2)   # color map origin
        f.read(2)   # color map length
        f.read(1)   # color map depth

        f.read(2)   # x_origin
        f.read(2)   # y_origin
        self.width = struct.unpack("h", f.read(2))[0]  # width
        self.height = struct.unpack("h", f.read(2))[0] # height

        self.format = struct.unpack("b", f.read(1))[0] >> 3  # bits per pixel
        descriptor = struct.unpack("b", f.read(1))[0]   # image descriptor

        self.__data = bytearray(self.width * self.height * self.format)

        if datatype == 10:  # if compressed
            self.load_rle_image(f)
        else:
            for i in range(0, len(self.__data)):
                byte = struct.unpack("B", f.read(1))[0]
                self.__data[i] = byte

        f.close()
        print "%s   width = %s   height = %s  format = %s   data = %s " \
              % (filename, self.width, self.height, self.format, len(self.__data))

    def load_rle_image(self, file):
        pixel_count = self.width * self.height
        current_pixel = 0
        current_byte = 0

        while current_pixel != pixel_count:
            chunkheader = struct.unpack("B", file.read(1))[0]
            if chunkheader < 128:
                chunkheader += 1
                for i in range(0, chunkheader):
                    for t in range(0, self.format):
                        self.__data[current_byte] = struct.unpack("B", file.read(1))[0]
                        current_byte += 1
                    current_pixel += 1
                    if current_pixel > pixel_count:
                        print "read to many pixels"
                        return False
            else:
                chunkheader -= 127
                color = bytearray(self.format)
                for x in range(0, self.format):
                    color[x] = struct.unpack("B", file.read(1))[0]

                for i in range(0, chunkheader):
                    for t in range(0, self.format):
                        self.__data[current_byte] = color[t]
                        current_byte += 1
                    current_pixel += 1
                    if current_pixel > pixel_count:
                       print "read to many pixels"
                       return False
        # print "pixels = %s\t current = %s\t bytes = %s\t current = %s" \
        #       % (pixel_count, current_pixel, len(self.__data), current_byte)
        return True

    def set(self, x, y, color):
        if (x < 0 or x >= self.width) or (y < 0 or y >= self.height):
            print 'bad value %s  %s ' % (x, y)
            return

        index = (x + y * self.width) * self.format
        self.__data[index + 0] = color.b()
        self.__data[index + 1] = color.g()
        self.__data[index + 2] = color.r()

        if self.format == Format.RGBA:
            self.__data[index + 3] = color.a()

    def get(self, x, y):
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            print "bad value %s  %s " % (x, y)
            return Color()
        else:
            index = int((x + y * self.width) * self.format)

            if index > len(self.__data):
                print "!!! %s    %s" % (index, len(self.__data))

            r = self.__data[index + 2]
            g = self.__data[index + 1]
            b = self.__data[index + 0]
            a = self.__data[index + 3] if self.format == Format.RGBA else 255
            return Color(r, g, b, a)

    def flip_vertically(self):
        bytes_per_line = self.width * self.format
        half = self.height >> 1
        for j in range(0, half):
            l1 = j * bytes_per_line
            l2 = (self.height - 1 - j) * bytes_per_line
            line = self.__data[l1: l1 + bytes_per_line]
            for i in range(0, bytes_per_line):
                self.__data[l1 + i] = self.__data[l2 + i]
            for i in range(0, bytes_per_line):
                self.__data[l2 + i] = line[i]

