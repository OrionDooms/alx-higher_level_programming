#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    q = set(my_list)
    for i in q:
        total += i
    return total
