#!/usr/bin/python3
from sys import argv
def check(value, list, matrix=[]):
    for i in range(value):
        for j in range(i + 1, value):
            if i != j:
                if list[i][0] == list[j][0]:
                    return matrix
                if list[i][1] == list[j][1]:
                    return matrix
    for i in range(n):
        copy = list[i]
        for j in range(1, n):
            if copy[0] + j >= n or copy[1] + j >= n :
                break
            if (copy[0] + j,copy[1] + j) in list:
                return matrix
        for j in range(1, n):
            if copy[0] + j >= n or copy[1] - j < 0 :
                break
            if (copy[0] + j,copy[1] - j) in list:
                return matrix
    print(list)
    matrix.append(list)
    print("xx")
    print(matrix)
    return matrix




def recurs(value, iter=0, previous=-1, list=[], matrix=[]):
    if value == iter:
        matrix = check(value, list, matrix)
        return matrix
    for i in range(previous + 1, n*n):
        list[iter] = (int(i/n), i%n)
        matrix = recurs(value, iter + 1, i, list, matrix)
    print(matrix)
    return matrix


if len(argv) != 2:
    print("Usage: nqueens N")
try:
    n = int(argv[1])
except:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)
for i in range(n,0, -1):
    print()
    n = 4
list = [0] * 4
matrix = []
matrix = recurs(4, 0, -1, list, matrix)
print("oo")
print(matrix)
for i in range(len(matrix)):
    print(matrix[i])
