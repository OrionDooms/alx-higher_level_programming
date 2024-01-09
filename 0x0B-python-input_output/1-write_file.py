#!/usr/bin/python3
"""Define read_file(filename="")"""


def write_file(filename="", text=""):
    """The function overwrite the content of the file.
    Args:
        filename (int): takes in a file.
        text (int): take in string.
        """
    with open(filename, mode="w", encoding='utf-8') as f:
        return f.write(text)
