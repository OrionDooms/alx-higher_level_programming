#!/usr/bin/python3
import json
"""Define def to_json_string(my_obj):"""


def to_json_string(my_obj):
    """The function returns JSON of an object"""
    return json.dumps(my_obj, sort_keys=True)
