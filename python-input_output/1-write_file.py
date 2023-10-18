#!/usr/bin/python3
"""function that write in a file"""


def write_file(filename="", text=""):
    """function that write in a file"""
    with open(filename, 'w') as file:
        return file.write(text)
