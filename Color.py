
class Color:
    def __init__(self, r=255, g=255, b=255, a=255):
        self.__r = r
        self.__g = g
        self.__b = b
        self.__a = a

    def r(self):
        return self.__r

    def g(self):
        return self.__g

    def b(self):
        return self.__b

    def a(self):
        return self.__a
