#!/usr/bin/python3

""" A square class"""


class Square:
    """ square class defined"""
    def __init__(self, size=0):
        """initialize the assigned values to object property

        Args:
            size: the size of the new square.
        """
        self.size = size

    def size(self):
        """ The size() method, get or set the current size."""
        return self.__size

    def size(self, value):
        """size must be an integer, otherwise raise a TypeError.
        if size is less than 0, raise a ValueError
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of the square"""
        return (self.size ** 2)
