#!/usr/bin/python3
for a in range(89):
    if (a == 0 or a == 10 or a == 11 or a == 20 or a == 21 or a == 22 or a == 30 or a == 31 or a == 32 or a == 33 or a == 40 or a == 41 or a == 42 or a == 43 or a == 44 or a == 50 or a == 51 or a == 52 or a == 53 or a == 54 or a == 55 or a == 60 or a == 61 or a == 62 or a == 63 or a == 64 or a == 65 or a == 66 or a == 70 or a == 71 or a == 72  or a == 73 or a == 74 or a == 75 or a == 76 or a == 77 or a == 80 or a == 81 or a == 82 or a == 83 or a == 84 or a == 85 or a == 86 or a == 87 or a == 88):
        print(end="")
    else:
        print(f"{a:02d}".format(a), end=", ")
print("89")
