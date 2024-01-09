#!/usr/bin/python3
"""Define read_file(filename="")"""


def read_file(filename=""):
    """The function that reads and prints the text file"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
    f.close()
