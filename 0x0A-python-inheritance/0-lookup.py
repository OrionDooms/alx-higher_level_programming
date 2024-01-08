#!/usr/bin/python3
"""lookup(obj) function that returns the list
of available attributes and methods """


def lookup(obj):
    """The function dir() makes a list of
    attributes and methods of a class
    Returns a list object
    """
    get_list = dir(obj)
    return get_list
