#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end="")
if number < 0:
    number = -int(repr(number)[-1])
else:
    number = int(repr(number)[-1])
if number > 5:
    print(f"{number} and is greater than 5")
elif number == 0:
    print(f"{number} and is zero")
elif number != 0 and number < 6:
    print(f"{number} and is less than 6 and not 0")
