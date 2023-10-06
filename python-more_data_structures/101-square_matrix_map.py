#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not matrix:
        return
    return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
