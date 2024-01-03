#!/usr/bin/python3
"""Module to add two integers
"""


def add_integer(a, b=98):
    """Function that adds two integers
        If a or b are not integers or float, the function raise a Error massage.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return(int(a) + int(b))
