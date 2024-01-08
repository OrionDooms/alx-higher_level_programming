#!/usr/bin/python3
"""A function that returns True if the object is an
instance of the specified class"""


def is_kind_of_class(obj, a_class):
    """If the object is an instance of the specified class
    returns True otherwise False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
