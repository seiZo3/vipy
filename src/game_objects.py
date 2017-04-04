#/usr/bin/python3

import abc
from enum import Enum
import math

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class Shape(Enum):
    CIRCLE = 1
    TRIANGLE = 2


def AngleToRadian(self, angle):
    return angle * math.pi / 180

def RotatePoint(self, point, axis, rad):
    """Calculates the position of a single point after rotation
    around the axis point."""
    pass


class Entity(object):
    """Base class for all game objects on screen"""
    def __init__(self, x, y, radius=10, color=RED, max_speed=0, shape=Shape.CIRCLE):
        self.x = x
        self.y = y
        self.color = color
        self.__radius = radius
        self.velx = self.vely = 0
        self.max_speed = max_speed
        self.__shape = shape
    
    @abc.abstractmethod
    def update(self, dt):
        """Primary update method for all entities"""
        return

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
    def velx(self):
        return self.__velx

    @velx.setter
    def velx(self, val):
        self.__velx = val

    @property
    def vely(self):
        return self.__vely

    @vely.setter
    def vely(self, val):
        self.__vely = val

    @property
    def speed(self):
        return math.sqrt(self.velx**2 + self.vely**2)

    @property
    def velocity(self):
        return (self.velx, self.vely)

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, val):
        if val < 0:
            raise ValueError('Cannot set max_speed less than zero')
        self.__max_speed = val

    @property
    def shape(self):
        return self.__shape

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

    @property
    def shape(self):
        return self.__shape


class Player(Entity):
    """Represents the player, and their specific functionality outside of handling input"""
    def __init__(self, pos, radius, max_speed):
        Entity.__init__(self, pos[0], pos[1],
                        radius=radius,
                        max_speed=max_speed,
                        color=GREEN,
                        shape=Shape.CIRCLE)


class Bullet(Entity):
    """Represents a simple bullet"""
    pass




class Enemy(Entity):
    """Represents a simple enemy"""

    def __init__(self, radius, max_speed):
        pos = generateSpawnPos()
        rotation = 0.0
        Entity.__init__(self, pos[0], pos[1],
                        radius=radius,
                        max_speed=max_speed,
                        color=RED,
                        shape=Shape.TRIANGLE)
    



