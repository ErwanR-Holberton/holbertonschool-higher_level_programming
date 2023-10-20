#!/usr/bin/python3
"""in this file i use a class to keep track of the amount of calls to funcio"""


class MagicString:
    """class with a public value"""
    i = 0
    @classmethod
    def __init__(cls):
        cls.i += 1


def magic_string():
    """create an object to count calls, print n*bestschool"""
    item = MagicString()
    return ("BestSchool, " * MagicString.i)[:-2]
