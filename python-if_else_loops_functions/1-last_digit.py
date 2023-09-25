#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end="")
if number < 0:
    last = (-number) % 10
    print("-", end="")
else:
    last = number % 10
if last > 5:
    print(f"{last} and is greater than 5")
elif last == 0:
    print(f"{last} and is zero")
else:
    print(f"{last} and is less than 6 and not 0")
