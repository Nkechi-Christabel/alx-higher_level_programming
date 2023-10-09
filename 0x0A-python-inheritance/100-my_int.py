#!/usr/bin/python3

"""
This module (myint.py) defines the MyInt class.
"""


class MyInt(int):
    """
    Class representing a rebel integer.

    MyInt has inverted == and != operators.

    Methods:
        __eq__(self, other): Override the equality operator (==) to invert
        its behavior.
        __ne__(self, other): Override the inequality operator (!=) to invert
        its behavior.
    """

    def __eq__(self, other):
        """Override the equality operator (==) to invert its behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=) to invert its behavior."""
        return super().__eq__(other)
