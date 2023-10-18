#!/usr/bin/python3
"""function that write in a file appending it"""


def append_write(filename="", text=""):
    """function that write in a file appending it"""
    with open(filename, 'a') as file:
        return file.write(text)
