#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    sum = 0
    prev = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for chars in roman_string[::-1]:
        value = dict.get(chars, 0)
        if value < prev:
            sum -= value
        else:
            sum += value
        prev = value
    return sum
