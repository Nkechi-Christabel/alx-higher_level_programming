#!/usr/bin/python3
"""
This module (8-rectangle.py) defines the Rectangle class.
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
        area(self): Calculate the area of the rectangle.
        __str__(self): Return a string representation of the rectangle.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than or equal to 0.
    """
    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
