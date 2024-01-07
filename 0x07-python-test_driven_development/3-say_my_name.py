#!/usr/bin/python3
"""Say_my_name."""


def say_my_name(first_name, last_name=""):
    """A function that prints first name and last name

    Args:
        first_name (str): takes in a first name
        last_name (str):  takes in a last name
    Raises:
        TypeError: first name or last name must be a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
