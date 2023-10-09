#!/usr/bin/python3
"""
This module (9-square.py) defines the Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.

    Attributes:
        None

    Methods:
        __init__(self, size): Initialize a Square instance with size.
        area(self): Calculate the area of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than or equal to 0.
    """

    def __init__(self, size):
        """Initialize a Square instance with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square by accessing the width and height
        attributes inherited from the Rectangle class."""
        return self._Rectangle__width * self._Rectangle__height
