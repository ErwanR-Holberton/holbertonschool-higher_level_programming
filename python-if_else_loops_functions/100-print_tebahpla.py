#!/usr/bin/python3
for a in range(25, -1, -1):
    if a % 2 == 0:
        print("{}".format(chr(a + 65)), end="")
    else:
        print("{}".format(chr(a + 97)), end="")
