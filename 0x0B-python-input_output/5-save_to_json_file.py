#!/usr/bin/python3
"""
This module (5-save_to_json_file.py) contains a function save_to_json_file(),
that writes an Object to a text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Serialize an object to JSON and save it to a text file.

    Args:
        my_obj: The object to be serialized and saved.
        filename (str): The name of the text file to save the JSON data.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
