#!/usr/bin/python3
"""Define read_file(filename="")"""


def read_file(filename=""):
    """The function that reads and prints the text file"""
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
    f.close()
    print(read_data)
