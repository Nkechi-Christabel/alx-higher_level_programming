#!/usr/bin/python3

"""
This module defines a class Square that represents a square.

It is based on the 0-square.py module.
"""


class Square:
    """
    Initializes an instance of the Square class.

    Args:
        size (int): The size of the square.

    Attributes:
        __size (int): A private instance attribute representing the size of the square.
    """
    def __init__(self, size):
        """
        Initializes the Square object with the provided size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
