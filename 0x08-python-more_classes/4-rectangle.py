#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def width(self):
        return self.__width

    def width(self, value):
        if type(value) != int:
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if type(value) != int:
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0:
            return (0)
        if self.height == 0:
            return (0)
        return (2 * (self.width + self.height))

    def __str__(self):
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print()
        return string
