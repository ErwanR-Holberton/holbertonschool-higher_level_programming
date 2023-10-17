#!/usr/bin/python3
"""function that reads a file"""


def read_file(filename=""):
    with open(filename, 'r') as file:
        print(file.read())
