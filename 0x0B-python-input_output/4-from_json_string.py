#!/usr/bin/python3
"""
This module (4-from_json_string.py) contains a function from_json_string(),
that returns a Python data structure (object) represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Deserialize a JSON-formatted string into a Python object.

    Args:
        my_str (str): The JSON-formatted string to be deserialized.

    Returns:
        Any: A Python data structure (object) represented by the JSON string.
    """
    return json.loads(my_str)
