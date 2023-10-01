#!/usr/bin/python3

"""
This is "3-say_my_name" module

The 3-say_my_name supplies one function, say_my_name(), that prints
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name as "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name).strip)
