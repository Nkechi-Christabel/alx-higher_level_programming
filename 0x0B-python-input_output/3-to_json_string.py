#!/usr/bin/python3
"""
This module(3-to_json_string.py) contains a function to_json_string(),
that returns the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Converts an object to its JSON representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: A JSON-formatted string representing the input object.
    """
    return json.dumps(my_obj)
