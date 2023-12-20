#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def size(self):
        return self.__size

    def size(self, value):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self):
        return self.__position

    def position(self, value):
        if (type(size) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position


    def area(self):
        return self.__size * self.__size

    def my_print(self):
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
                if (self.__position > 0):
                    print('-')
