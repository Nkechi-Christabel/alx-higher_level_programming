#!/usr/bin/python3
"""
This module (6-load_from_json_file.py) contains a function
load_from_json_file(), that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    Deserialize an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        Any: The Python data structure (object) loaded from the JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
