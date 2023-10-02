#!/usr/bin/python3
def max_integer(my_list=[]):
    save = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > save:
            save = my_list[i]
    return save
