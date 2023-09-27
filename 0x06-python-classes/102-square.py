#!/usr/bin/python3

"""
This module defines a class Square that represents a square.

It is based on the based on 4-square.py
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
        """
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float: The area of the square.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for updating the size of the square.

        Args:
            value (float): The new size to set for the square.

        Raises:
            TypeError: If the new size is not a number (float or integer).
            ValueError: If the new size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        """
        Compares if two squares have equal areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if both squares have equal areas, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares if two squares have unequal areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if both squares have unequal areas, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compares if the area of this square is greater than the area of
        another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square's area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares if the area of this square is greater than or equal to
        the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square's area is greater or equal, False
            otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compares if the area of this square is less than the area of
        another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square's area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares if the area of this square is less than or equal to the
        area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square's area is less or equal, False otherwise.
        """
        return self.area() <= other.area()
