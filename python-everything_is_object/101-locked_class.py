#!/usr/bin/python3
"""a class that prevent creation of new attributes"""


class LockedClass():
    __slots__ = ("first_name")
