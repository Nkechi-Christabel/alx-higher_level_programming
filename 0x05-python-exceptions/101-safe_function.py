#!/usr/bin/python3
import sys

"""Executes a function safely.

Args:
   arg: The function arguments

Returns:
   The result of the function, otherwise: None
"""


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except (ZeroDivisionError, IndexError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
