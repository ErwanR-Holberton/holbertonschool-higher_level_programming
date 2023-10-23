#!/usr/bin/python3
"""define a class inheriting from Base"""
from models.base import Base


class Rectangle(Base):
    """define a class inheriting from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        is_integer(width, "width")
        is_above_zero(width, "width")
        is_integer(height, "height")
        is_above_zero(height, "height")
        is_integer(x, "x")
        above_or_zero(x, "x")
        is_integer(y, "y")
        above_or_zero(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @height.setter
    def height(self, value):
        is_integer(value, "height")
        is_above_zero(value, "height")
        self.__height = value

    @width.setter
    def width(self, value):
        is_integer(value, "width")
        is_above_zero(value, "width")
        self.__width = value

    @x.setter
    def x(self, value):
        is_integer(value, "x")
        above_or_zero(value, "x")
        self.__x = value

    @y.setter
    def y(self, value):
        is_integer(value, "y")
        above_or_zero(value, "y")
        self.__y = value

    def area(self):
        """return area"""
        return self.__height * self.__width

    def display(self):
        """prints the rectangle"""
        print(("#" * self.__width + "\n") * self.__height, end="")

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}/{}".format
                (self.__class__.__name__, self.id, self.x,
                 self.y, self.__width, self.__height))


def is_integer(value, name):
    """check if integer"""
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))


def is_above_zero(value, name):
    """checks if is under or equal to zero"""
    if value <= 0:
        raise ValueError("{} must be > 0".format(name))


def above_or_zero(value, name):
    """checks if under zero"""
    if value < 0:
        raise ValueError("{} must be >= 0".format(name))
