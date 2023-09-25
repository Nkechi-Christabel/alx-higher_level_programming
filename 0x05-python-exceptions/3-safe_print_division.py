#!/usr/bin/python3

"""Divides 2 integers and prints the result..

Args:
    a: Integer 1
    b: Integer 2

Returns:
    The value of the division, otherwise: None
"""


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return (result)
