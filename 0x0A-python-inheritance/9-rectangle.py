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
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """area()
        Return:
            multiple width and height.
            """
        return(self.__width * self.__height)

    def __str__(self):
        """str()
        Return:
            A string [Rectangle] <width>/<height>
            """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
