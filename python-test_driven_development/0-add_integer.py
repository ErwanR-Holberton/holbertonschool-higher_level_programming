#!/usr/bin/python3
"""
this
is a
5 line comment
"""


def add_integer(a, b=98):
    """
    add two numbers and return an int sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
