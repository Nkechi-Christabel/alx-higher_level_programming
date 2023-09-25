#!/usr/bin/python3

"""Prints an integer with "{:d}".format().

Args:
   value: The value to print.

Returns:
   True if value is correctly printed, that is it's integer,
   otherwise False.
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        pass
        return (False)
