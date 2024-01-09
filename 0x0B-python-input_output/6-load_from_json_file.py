#!/usr/bin/python3
"""define load_from_json_file(filename)"""
import json


def load_from_json_file(filename):
    """The function creates an Object from a “JSON file”"""
    with open(filename) as f:
        return json.load(f)
    f.close()
