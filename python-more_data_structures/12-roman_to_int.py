#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    sum = 0
    value = 0
    for chars in roman_string:
        if chars == 'I':
            value = 1
        elif chars == 'V':
            value = 5
        elif chars == 'X':
            value = 10
        elif chars == 'L':
            value = 50
        elif chars == 'C':
            value = 100
        elif chars == 'D':
            value = 500
        if value > sum:
            sum = value - sum
        else:
            sum += value
    return sum
