#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """A function that raises an Exception with the message"""
    def area(self):
        """Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator.
        Args:
            name (str):takes in a string.
            value (int):takes in a integer.
        Raise:
            TypeError: <name> must be an integer.
            ValueError: <name> must be greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
