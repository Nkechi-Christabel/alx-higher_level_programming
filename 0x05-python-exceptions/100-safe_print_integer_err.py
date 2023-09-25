#!/usr/bin/python3
import sys

"""Prints an integer.

Args:
   value: The value to print.

Returns:
   True if value is correctly printed, that is it's integer,
   otherwise False.
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
