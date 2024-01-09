#!/usr/bin/python3
"""Define write_file(filename="", text="")"""


def write_file(filename="", text=""):
    """The function that writes a string to a tex file.
    Args:
        filename : takes in a file.
        text (int): take in string.
        """
    with open(filename, mode="w", encoding='utf-8') as f:
        return f.write(text)
