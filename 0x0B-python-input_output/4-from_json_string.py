#!/usr/bin/python3
"""define from_json_string(my_str):"""
import json


def from_json_string(my_str):
    """function that returns an object represented by a JSON """
    return json.loads(my_str)
