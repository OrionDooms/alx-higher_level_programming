#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """ defines of rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Iinitialize of rectangle

        Args:
            height (int): the height of the rectangle.
            width (int): the width of the rectangle.
            print_symbol (str): print the rectangle symbol.
            """
        self.height = height
        self.width = width
        self.print_symbol = "#"
        Rectangle.number_of_instances += 1

    def width(self):
        """ get the width of rectangle."""
        return self.__width

    def width(self, value):
        """Rectangle width
        if width is not a integer or less that zero then raise a Error"""
        if type(value) != int:
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """ get the height of rectangle."""
        return self.__height

    def height(self, value):
        """Rectangle height
        if height is not a integer or less that zero then raise a Error"""
        if type(value) != int:
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
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

    def __str__(self):
        """prints out a rectangle shape"""
        string = ""
        if self.width == 0:
            return (0)
        if self.height == 0:
            return (0)
        for i in range(self.height):
            for j in range(self.width):
                print(self.print_symbol, end="")
            print()
        return string

    def __repr__(self):
        """return a string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """print out a message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return (rect_1)
        if rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
