#!/usr/bin/python3

"""A square class"""


class Square:
    """square class defined"""
    def __init__(self, size=0):
        """initialize the assigned values to object property

        Args:
            size: the size of the new square."""
        self.__size = size

    def size(self):
        """The size() method, get or set the current size."""
        return self.__size

    def size(self, value):
        """ size must integer, size is not less than 0"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """The size() method, get or set the current size.
        f size is equal to 0, print an empty line.
        else that prints in stdout the square with the character #."""
        if self.__size == 0:
            print("")
        else:
            i = 0
            for i in range(self.__size):
                j = 0
                for j in range(self.__size):
                    j = j + 1
                    print("#", end="")
                i = i + 1
                print('')
