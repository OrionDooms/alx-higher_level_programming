#!/usr/bin/python3

class Rectangle:
    def __init__(self, width, height):
        """self.__width = width
        self.__height = height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
