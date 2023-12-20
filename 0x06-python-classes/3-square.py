#!/usr/bin/python3

"""A square class"""


class Square:
    """ a classes built in __init__() function"""
    def __init__(self, size=0):
        """type() function returns the type of object
        or returns a argument passes
        Args:
            self: The first parameter.
            size: The second parameter.
            """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            """instance method always has self as an argument"""
    def area(self):
        """Return area of the square"""
        return(self.__size * self.__size)
