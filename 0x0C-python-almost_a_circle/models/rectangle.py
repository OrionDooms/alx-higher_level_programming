#!/usr/bin/python3
"""Define Rectangle class"""
from models.base import Base



class Rectangle(Base):
    """Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize for rectangle.
        Args:
            width (int): Takes in width of the rectangle.
            height (int):Takes in heigh of the rectangle..
            x (int): Takes in x value.
            y (int): Takes in x value..
            id: comes from base class that count how many time
            the programs been used.
            """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int():
            raise TypeError("width must be an integer")
        if int(value) <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int():
            raise TypeError("height must be an integer")
        if int(value) <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int():
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int():
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

    def area(self):
        """Area returns the area value of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Display function prints a stdout Rectangle
        with the character #"""
        for i in range(self.__x):
            print("" * self.__y, end="")
            print()
        for i in range(self.__height):
            print("#" * self.__width, end="")
            print()

    def __str__(self):
        """__str__ method returns [Rectangle] (id) x/y - width/height"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args):
        for arg in args:
            self.__id = arg[]
            self.__width = arg
            self.__height = arg
            self.__x = arg
            self.__y = arg
