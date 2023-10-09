#!/usr/bin/python3

"""
This module (add_attribute_module.py) defines a function to add a new
attribute to an object if possible and raises a TypeError if not.
"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible."""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
