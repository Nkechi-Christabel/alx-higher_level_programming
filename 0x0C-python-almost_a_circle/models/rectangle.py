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

      Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initialize a new instance of the Rectangle class with validation.

        area(self):
            Calculate and return the area of the rectangle.

        display(self):
            Print the Rectangle instance using '#' characters to stdout, taking
            x and y into account.

        update(self, *args):
            Assign arguments to the attributes in the following order: id,
            width, height, x, y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new instance of the Rectangle class with validation.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): An identifier for the instance.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        Setter for the width attribute with validation.

        Args:
            value (int): The new width to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        Setter for the height attribute with validation.

        Args:
            value (int): The new height to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        Setter for the x attribute with validation.

        Args:
            value (int): The new x-coordinate to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        Setter for the y attribute with validation.

        Args:
            value (int): The new y-coordinate to set.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance using '#' characters to stdout.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle.

        Returns:
            str: A string in the format [Rectangle] (<id>) <x>/<y> - <width>/
            <height>.
        """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        Assign arguments to the attributes in the following order: id, width,
        height, x, y. If **kwargs is provided, assign key/value pairs to
        attributes.

        Args:
            *args: The arguments to assign to the attributes.
            **kwargs: Keyword arguments to assign key/value pairs to atrribu
            tes.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                if not isinstance(value, int):
                    raise TypeError(f"{attr} must be an integer")
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key not in attributes:
                    raise TypeError(f"Invalid attribute: {key}")
                if not isinstance(value, int):
                    raise TypeError(f"{key} must be an integer")
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Rectangle.

        Returns:
            dict: A dictionary containing the attributes of the Rectangle.
        """
        keys = ['x', 'y', 'id', 'height', 'width']
        return {k: getattr(self, k) for k in keys}
