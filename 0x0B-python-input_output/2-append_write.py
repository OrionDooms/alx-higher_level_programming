#!/usr/bin/python3
"""Define append_write(filename="", text="")"""


def append_write(filename="", text=""):
    """The function that appends a string at the end of a text file.
    Args:
        filename : takes in a file.
        text (int): take in string.
        """
    with open(filename, mode="a", encoding='utf-8') as f:
        return f.write(text)
