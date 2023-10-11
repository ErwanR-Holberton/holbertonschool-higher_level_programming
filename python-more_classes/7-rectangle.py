#!/usr/bin/python3
"""Contains a class definition of a rectangle"""


class Rectangle:
    """Definition of a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        test_positive_int(width, "width")
        test_positive_int(height, "height")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        test_positive_int(value, "height")
        self.__height = value

    @width.setter
    def width(self, value):
        test_positive_int(value, "width")
        self.__width = value

    def perimeter(self):
        if self.__height != 0 and self.__width != 0:
            return self.__height * 2 + self.__width * 2
        return 0

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        return ((str(self.print_symbol)*self.__width+"\n")*self.__height)[0:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


def test_positive_int(value, message):
    if not isinstance(value, int):
        raise TypeError(message + " must be an integer")
    if value < 0:
        raise ValueError(message + " must be >= 0")
