#!/usr/bin/python3

"""A square class"""


class Square:
    """ a classes built in __init__() function"""
    def __init__(self, size=0):
        """type() function returns the type of object
        or returns a argument passes"""
        if type(size) != int:
            """ raise a error message"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise a error message"""
            raise ValueError("size must be >= 0")
        else:
            """Access class Attributes using objects
        use . notation to access the attributes"""
            self.__size = size
