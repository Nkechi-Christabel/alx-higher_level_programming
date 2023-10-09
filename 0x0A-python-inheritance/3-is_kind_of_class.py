#!/usr/bin/python3

"""Returns True if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of the specified class or any of its
    subclasses.

    Parameters:
        obj (object): The object to be checked.
        a_class (class): The class or superclass to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass, False
        otherwise.
    """
    return isinstance(obj, a_class)
