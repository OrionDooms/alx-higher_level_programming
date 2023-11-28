#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number%10
if last > 5:
    p = (f"{last} and is greater than 5")
elif last == 0:
    p = (f"{last} and is 0")
else:
    p = (f"{last} and is less than 6 and not 0")
print(f"Last digit of {number} is {p}")
