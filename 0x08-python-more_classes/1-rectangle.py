#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """ defines of rectangle"""
    def width(self):
        return self.__width

    def width(self, value):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def height(self):
        return self.__height

    def height(self, value):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
