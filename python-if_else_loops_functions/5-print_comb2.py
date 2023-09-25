#!/usr/bin/python3
for val in range(0, 100):
    if val != 99:
        print("{:02d}, ".format(int(val)), end="")
    else:
        print("{:02d}".format(int(val)))
