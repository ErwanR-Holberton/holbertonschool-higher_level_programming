#!/usr/bin/python3
"""if a searched string is in a line of the file
it will append a new string after it"""


def append_after(filename="", search_string="", new_string=""):
    """main loop open file get a line and test it"""
    with open(filename, 'r+') as file:
        str = file.read()
        index = 0
        res = ""
        while True:
            end_line = get_index_end_line(index, str)
            line = get_line(index, end_line, str)
            res += line
            if search_in(line, search_string):
                res += new_string
            if end_line == -1:
                break
            index = end_line + 1
    file.close()
    with open(filename, 'w+') as file:
        file.write(res)


def get_index_end_line(start_index, text):
    """find the end of the line or -1 for the end of the file"""
    for i in range(start_index, len(text)):
        if text[i] == '\n':
            return i
    return -1


def get_line(start, end, text):
    """returns the string of the current line"""
    if end == -1:
        end = len(text) - 1
    line = ""
    for i in range(start, end + 1):
        line += text[i]
    return line


def search_in(line, search_string=""):
    """find if searched string is in line"""
    for i in range(len(line)):
        boolean = 1
        for j in range(len(search_string)):
            if i + j >= len(line):
                return 0
            if line[i + j] != search_string[j]:
                boolean = 0
        if boolean == 1:
            return 1
    return 0
