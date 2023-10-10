#!/usr/bin/python3

"""
This module (8-class_to_json.py) contains a function class_to_json(),
that returns the dictionary description with simple data structure (list,
dictionary, string, integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Convert an object's attributes to a dictionary for JSON serialization.

    Args:
        obj: An object whose attributes are to be converted.

    Returns:
        dict: A dictionary containing the attributes of the object.
    """
    return obj.__dict__
