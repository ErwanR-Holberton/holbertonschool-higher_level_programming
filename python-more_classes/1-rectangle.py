#!/usr/bin/python3
"""Contains a class definition of a rectangle"""


class Rectangle:
    """Definition of a rectangle"""
    def __init__(self, width=0, height=0):
        test_positive_int(width, "width")
        test_positive_int(height, "height")
        self.__height = height
        self.__width = width

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

def test_positive_int(value, message):
        if not isinstance(value, int):
            raise TypeError(message + " must be an integer")
        if value < 0:
            ValueError(message + " must be >= 0")
