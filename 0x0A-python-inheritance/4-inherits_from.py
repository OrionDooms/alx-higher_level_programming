#!/usr/bin/python3
"""A function that returns True if the object is an
instance of the specified class"""


def inherits_from(obj, a_class):
    """If the object is an instance of the specified class
    returns True otherwise False."""
    if type(obj) == a_class:
        return False
    else:
        return True
