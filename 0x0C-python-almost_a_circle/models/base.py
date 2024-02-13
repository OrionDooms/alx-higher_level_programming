#!/usr/bin/python3
from models import base
"""Define base class"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base.
        Args:
            id (int): increment __nb_objects and assign it to id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
