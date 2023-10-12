#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square:
    """Definition of square"""
    def __init__(self, size=0, position=(0, 0)):
        check_size(size)
        self.__size = size
        check_tuple(position)
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        check_size(value)
        self.__size = value

    @property
    def position(self):
        return (self.position)

    @size.setter
    def position(self, value):
        check_tuple(value)
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)


def check_size(value):
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")


def check_tuple(value):
    if not isinstance(value, tuple):
        raise TypeError("position must be a tuple of 2 positive integers")
    if len(value) != 2:
        raise TypeError("position must be a tuple of 2 positive integers")
    if not isinstance(value[0], int):
        raise TypeError("position must be a tuple of 2 positive integers")
    if not isinstance(value[1], int):
        raise TypeError("position must be a tuple of 2 positive integers")
    if value[0] < 0 or value[1] < 0:
        raise TypeError("position must be a tuple of 2 positive integers")
