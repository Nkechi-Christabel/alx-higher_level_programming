#!/usr/bin/python3

"""
This module(0-lookup) defines a function lookup() that returns the list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object for which you want to retrieve attributes and methods.

    Returns:
        A list containing the names of attributes and methods of the object.
    """
    return dir(obj)
