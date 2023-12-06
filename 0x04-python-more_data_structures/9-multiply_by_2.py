#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}
    for keys, value in a_dictionary.items():
        result[keys] = value * 2
    return result
