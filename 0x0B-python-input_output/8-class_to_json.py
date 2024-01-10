#!/usr/bin/python3
"""define class_to_json(obj)"""
import json


def class_to_json(obj):
    """function that returns the dictionary description
    with data structure"""
    return obj.__dict__
