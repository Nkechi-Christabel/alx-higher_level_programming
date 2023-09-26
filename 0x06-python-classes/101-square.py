#!/usr/bin/python3

"""
This module defines a class Square that represents a square.

It is based on the based on 5-square.py
"""


class Square:
    """
    Represents a square shape with a specified size.

    Attributes:
        __size (int): The size of the square. Access using the 'size' property.
        __position (tuple): The position of the square. Access using the
            'position' property.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square with the given size.

        Args:
            size (int): The size of the square. Defaults to 0 if not provided.
        """
        self.size = size
        self.position = position

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
        return (self.__size)

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

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter method for updating the position of the square.

        Args:
            value (tuple): A tuple of two integers representing the new
            position. The first integer is the horizontal position, and
            the second integer is the vertical position.

        Raises:
            TypeError: If the 'value' parameter is not a tuple of two integers,
                or if either of the integers is not an integer, or if either of
                the integers is less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(i, int) for i in value) \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints a representation of the square with '#' character to the stdout.

        If the size of the square is 0, it prints an empty line. Otherwise, it
        prints the square with respect to the 'position' attribute by adding
        the specified number of spaces before the '#' characters.
        """
        if self.__size == 0:
            return ""

        sqr_rows = []

        for _ in range(self.__position[1]):
            sqr_rows.append("")

        sqr_rows.extend([" " * self.__position[0] + "#" * self.__size] *
                        self.__size)

        return "\n".join(square_rows)

    def __str__(self):
        """
        Returns a string representation of the square for printing.

        Returns:
            str: A string representation of the square.
        """
        return str(self.my_print())
