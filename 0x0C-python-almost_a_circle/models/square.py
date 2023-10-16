#!/usr/bin/python3
"""
This module (square.py) defines the Square class,
that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class represents a geometric square, inheriting attributes and
    methods from Rectangle.

    Attributes (inherited from Rectangle):
        __width (int): The private width of the square (same as height).
        __height (int): The private height of the square (same as width).
        __x (int): The private x-coordinate of the square's position.
        __y (int): The private y-coordinate of the square's position.

    Methods (inherited from Rectangle):
        __init__(self, width, height, x=0, y=0, id=None): Initialize a new
        instance of the Square class.

        area(self): Calculate and return the area of the square.
        display(self): Print the Square instance using '#' characters to stdout
        , taking x and y into account.

        __str__(self): Return a string representation of the Square.

        size(self): Getter for the size attribute.
        size(self, value): Setter for the size attribute.

        update(self, *args, **kwargs): Update attributes using positional and
                                       keyword arguments.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance of the Square class with the same attributes
        and methods as Rectangle.

        Args:
            size (int): The size of the square, which will be assigned to both
            width and height.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): An identifier for the instance.

        Raises:
            TypeError: If size, x, or y is not an integer.
            ValueError: If size is less than or equal to 0 or if x or y is less
            than 0.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square.

        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size> (same
            as width or height).
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter for the size attribute, which is the same as width or height.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute, which assigns the same value to both
        width and height.

        Args:
            value (int): The new size to set.
        """
        self.width = value
        self.hieight = value

    def update(self, *args, **kwargs):
        """
        Update attributes using positional and keyword arguments.

        Args:
            *args: List of arguments in the following order: id, size, x, y.
            **kwargs: Keyword arguments to update specific attributes.

        Notes:
            If *args is provided and not empty, **kwargs will be skipped.
        """
        attributes = ["id", "size", "x", "y"]
        if args:
            for attr, value in zip(attributes, args):
                if not isinstance(value, int):
                    raise TypeError(f"{attr} must be an integer")
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if not isinstance(value, int):
                    raise TypeError(f"{key} must be an integer")
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Square.

        Returns:
            dict: A dictionary containing the attributes of the Square.
        """
        keys = ['id', 'x', 'size', 'y']
        return {k: getattr(self, k) for k in keys}
