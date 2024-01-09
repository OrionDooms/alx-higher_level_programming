#!/usr/bin/python3
"""Define to_json_string(my_obj):"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object"""
    return json.dumps(my_obj, sort_keys=True)
