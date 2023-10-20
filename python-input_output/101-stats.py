#!/usr/bin/python3
"""get each line of generator and parse it to print total size and errors"""
from sys import stdin
i = 0
error = {}
error['200'] = 0
error['301'] = 0
error['400'] = 0
error['401'] = 0
error['404'] = 0
error['405'] = 0
error['500'] = 0
total_size = 0
for line in stdin:
    for char in range(0, len(line)):
        if line[char] == ' ':
            ip = line[0:char]
            line = line[char + 3:]
            break
    for char in range(0, len(line)):
        if line[char] == ']':
            date = line[0:char + 1]
            line = line[char + 2:]
            break
    for char in range(1, len(line)):
        if line[char] == '\"':
            file = line[0:char + 1]
            line = line[char + 2:]
            break
    for char in range(0, len(line)):
        if line[char] == ' ':
            code = line[0:char]
            line = line[char + 1:]
            break
    size = int(line)
    for key, value in error.items():
        if key == code:
            error[key] += 1
    total_size += size
    i += 1
    if i % 10 == 0:
        print("File size: {}".format(total_size))
        for key, value in error.items():
            if value != 0:
                print("{}: {}".format(key, value))
