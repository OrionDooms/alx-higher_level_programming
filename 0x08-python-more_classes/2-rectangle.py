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

    def width(self):
        """get the width of rectangle."""
        return self.__width

    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """get the height of rectangle."""
        return self.__height

    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area"""
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter"""
        if self.width == 0:
            return (0)
        if self.height == 0:
            return (0)
        return (2 * (self.width + self.height))
