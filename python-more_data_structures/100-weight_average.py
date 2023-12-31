#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = 0
    weights = 0
    for tuples in my_list:
        res += tuples[0] * tuples[1]
        weights += tuples[1]
    return res / weights
