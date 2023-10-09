#!/usr/bin/python3

"""
This module defines a class Rectangle.

It is based on 7-base_geometry.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.

    Attributes:
        None

    Methods:
        __init__(self, width, height): Initialize a Rectangle instance
        with width and height.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than or equal to 0.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
