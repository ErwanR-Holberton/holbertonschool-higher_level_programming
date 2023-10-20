#!/usr/bin/python3
class MagicString:
    i = 0
    @classmethod
    def __init__(cls):
        cls.i += 1



def magic_string():
    item = MagicString()
    return ("BestSchool, " * MagicString.i)[:-2]
