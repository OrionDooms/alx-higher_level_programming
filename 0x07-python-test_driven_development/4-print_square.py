#!/usr/bin/python3
"""print_square"""


def print_square(size):
    """prints a square with the character #

    Args:
        size (int): size is the size length of the square
    Raises:
        TypeError: size must be an integer
        ValueError: ize must be >= 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(1, size + 1):
            print("#", end="")
        print()
