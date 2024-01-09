#!/usr/bin/python3
"""Define add_item"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """adds arguments of a Python list, to a JSON file"""
    args = sys.argv[1:]
    my_obj = []
    my_obj = args
    filename = "add_item.json"
    load_from_json_file(filename)
    save_to_json_file(my_obj, filename)
