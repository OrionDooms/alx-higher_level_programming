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
        """Rectangle width
        if width is not a integer or less that zero then raise a Error"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def height(self):
        """get the height of rectangle."""
        return self.__height

    def height(self, value):
        """Rectangle height
        if height is not a integer or less that zero then raise a Error"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Return the area"""
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter"""
        if self.width == 0:
            return (0)
        return (2 * (self.width + self.height))
