#!/usr/bin/python3
def max_integer(my_list=[]):
    save = 0
    for ints in my_list:
        if ints > save:
            save = ints
    return save

