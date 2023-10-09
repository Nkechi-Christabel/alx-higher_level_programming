#!/usr/bin/python3
"""
This module (11-square.py) defines the Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.

    Methods:
        __init__(self, size): Initialize a Square instance with size.
        area(self): Calculate the area of the square.
    """

    def __init__(self, size):
        """Initialize a Square instance with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
