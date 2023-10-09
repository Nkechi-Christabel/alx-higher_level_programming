#!/usr/bin/python3

"""Returns True if the object is exactly an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Parameters:
        obj (object): The object to be checked.
        a_class (class): The class to compare against.

    Returns:
        bool: True if obj is an exact instance of a_class, False otherwise.
    """
    return type(obj) is a_class
