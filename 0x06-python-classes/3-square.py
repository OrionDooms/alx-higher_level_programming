#!/usr/bin/python3

"""A square class"""


class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            """instance method always has self as an argument"""
    def area(self):
        """returns the current square area"""
        return(self.__size**2)
