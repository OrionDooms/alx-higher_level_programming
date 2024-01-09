#!/usr/bin/python3
"""define save_to_json_file(my_obj, filename)"""
import json


def save_to_json_file(my_obj, filename):
    """The function that writes an Object to a text file,
    using a JSON representation.
    Args:
        my_obj: JavaScript Object.
        filename: text file.
        """
    with open(filename, mode="w", encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
