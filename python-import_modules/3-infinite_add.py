#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    result = 0
    for i in range(1, argc):
        result += int(argv[i])
    print("{}".format(result))
