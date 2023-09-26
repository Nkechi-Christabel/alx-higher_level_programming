#!/usr/bin/python3

"""
This module defines a class Square that represents a square.

It is based on the based on 1-square.py
"""


class Square:
    """
    Represents a square shape with a specified size.

    Attributes:
        __size (int): The size of the square. Access using the 'size' property.
    """
    def __init__(self, size=0):
        """
        Initializes a new square with the given size.

        Args:
            size (int): The size of the square. Defaults to 0 if not provided.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
