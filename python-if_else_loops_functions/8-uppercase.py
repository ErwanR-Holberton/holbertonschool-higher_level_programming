#!/usr/bin/python3
def uppercase(str):
    value = 0
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            value = ord(letter) - 32
        else:
            value = ord(letter)
        print(chr(value), end="")
    print("")
