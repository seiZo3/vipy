#/bin/python3


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class Entity(object):
    def __init__(self, x, y, radius=10, color=RED):
        self.x = x
        self.y = y
        self.color = color
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    @property
    def speed(self):
        return 5

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, val):
        self.__color = val

    @property
    def radius(self):
        return self.__radius
