#!/usr/bin/python3

"""Returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly
    or indirectly) from the specified class.

    Parameters:
        obj (object): The object to be checked.
        a_class (class): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, False
        otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
