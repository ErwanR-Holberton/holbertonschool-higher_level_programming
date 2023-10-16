#!/usr/bin/python3
def copy_list(a_list):
    new_list = [0] * len(a_list)
    for i in range(len(a_list)):
        new_list[i] = a_list[i]
    return new_list

