#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """ defines of rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize of rectangle

        Args:
            height (int): the height of the rectangle.
            width (int): the width of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """get the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width
        if width is not a integer or less that zero then raise a Error"""
        """if value != int:
            raise TypeError("width must be an integer")"""
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height
        if height is not a integer or less that zero then raise a Error"""
        """if type(value) != int:
            raise TypeError("height must be an integer")"""
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
