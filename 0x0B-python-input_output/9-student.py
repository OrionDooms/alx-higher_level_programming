#!/usr/bin/python3
"""Define student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialize attributes.
        Args:
            first_name (str): Takes in a first name of a person.
            last_name (str): Takes in a last name of a person..
            age (int): Take in a age of a person)
            """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation data"""
        return self.__dict__
