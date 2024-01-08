#!/usr/bin/python3
"""MyList class that inherits a list"""


class MyList(list):
    """prints a sorted list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        sort = sorted(self)
        print(sort)
