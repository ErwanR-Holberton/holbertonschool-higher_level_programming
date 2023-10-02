#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    val1 = 0
    val2 = 0
    if len(tuple_a) >= 1:
        val1 += tuple_a[0]
    if len(tuple_b) >= 1:
        val1 += tuple_b[0]
    if len(tuple_a) >= 2:
        val2 += tuple_a[1]
    if len(tuple_b) >= 2:
        val2 += tuple_b[1]
    res_tuple = (val1, val2)
    return res_tuple
