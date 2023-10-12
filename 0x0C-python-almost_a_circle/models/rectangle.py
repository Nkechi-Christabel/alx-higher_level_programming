#!/usr/bin/python3
"""
This module (rectangle.py) defines the Rectangle class,
that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    The Rectangle class represents a geometric rectangle.

    Attributes:
        __width (int): The private width of the rectangle.
        __height (int): The private height of the rectangle.
        __x (int): The private x-coordinate of the rectangle's position.
        __y (int): The private y-coordinate of the rectangle's position.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): An identifier for the instance.

        Attributes:
            __width (int): The private width of the rectangle.
            __height (int): The private height of the rectangle.
            __x (int): The private x-coordinate of the rectangle's position.
            __y (int): The private y-coordinate of the rectangle's position.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The new width to set.

        Raises:
            ValueError: If the provided width is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The new height to set.

        Raises:
            ValueError: If the provided height is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): The new x-coordinate to set.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): The new y-coordinate to set.
        """
        self.__y = value
