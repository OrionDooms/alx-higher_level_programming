#!/usr/bin/python3
""""""
class Square:
    """"""
    def __init__(self, size=0):
        """"""
        self.__size = size
    def size(self):
        """"""
        return self.__size
    def size(self, value):
        if type(size) != 0:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """"""
        return self.__size * self.__size
    def my_print(self):
        """"""
        if self.__size == 0:
            print("")
        else:
            i = 0
            for i in range(self.__size):
                j = 0
                while j < self.__size:
                    j = j + 1
                    print("#", end=" ")
                i = i + 1
                print('')
