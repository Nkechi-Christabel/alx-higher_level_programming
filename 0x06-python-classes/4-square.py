#!/usr/bin/python3

"""
This module defines a class Square that represents a square.

It is based on the based on 2-square.py
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

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for updating the size of the square.

        Args:
            value (int): The new size to set for the square.

        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
