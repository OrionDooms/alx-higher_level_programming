#!/usr/bin/python3
"""Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """Rectangle class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initialized width and height.
        Args:
            width (int): take in a integer.
            height (int): take in a integer.
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
