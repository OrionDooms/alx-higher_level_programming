#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    n_last = -last
else:
    n_last = last

if n_last > 5:
    p = (f"{n_last} and is greater than 5")
elif n_last == 0:
    p = (f"{n_last} and is 0")
else:
    p = (f"{n_last} and is less than 6 and not 0")
print(f"Last digit of {number} is {p}")
