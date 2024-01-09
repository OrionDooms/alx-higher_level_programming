#!/usr/bin/python3
"""Define read_file(filename="")"""


def write_file(filename="", text=""):
    """The function overwrite the content of the file"""
    with open(filename, mode="w", encoding='utf-8') as f:
        f.write(text)
